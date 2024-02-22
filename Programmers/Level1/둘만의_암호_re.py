# 두 문자열 s와 skip, 그리고 자연수 index가 주어질 때, 다음 규칙에 따라 문자열을 만들려고 한다.
# 문자열 s의 각 알파벳을 index 만큼 뒤의 알파벳으로 바꿔준다.
# index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아간다.
# skip에 있는 알파벳은 제외하고 건너뛴다.

# 문자를 아스키코드로 (ord), 아스키코드를 문자로(chr) 변환하는 방식으로 접근

def solution(s, skip, index):
    answer = ''
    skip=list(skip)
    for i in range(len(s)):
        # skip에 있는 알파벳 제외
        target=ord(s[i])
        cnt=index
        while cnt>0:
            target+=1
            # target이 z를 넘어갈 경우
            if ord('z')<target:
                target=ord('a')
            # target이 skip에 속해있는 경우
            if chr(target) in skip:
                cnt+=1
            cnt-=1
        answer+=chr(target)
    return answer

s="aukks"
skip="wbqd"
index=5
print(solution(s,skip,index))