# 문자열 s가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 합니다.
# 먼저 첫 글자를 읽는다. 해당 글자 x
# 문자열을 왼쪽에서 오른쪽으로 읽어나가면서 x와 x가 아닌 다른 글자들이 나온 횟수를 각각 센다.
# 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리한다.
# s에서 분리한 문자열을 빼고 남은 부분에 대해서 이과정을 반복(남은 부분이 없다면 종료)
# 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고 종료

def solution(s):
    answer = 0
    x,not_x='',''
    x_cnt=0
    y_cnt=0
    for i in range(len(s)):
        if not x:

            x+=s[i]
            x_cnt+=1
            print(x)
        else:
            if s[i]!=x:
                not_x+=s[i]
                y_cnt+=1
            elif s[i]==x:
                x_cnt+=1
        if x_cnt==y_cnt:
            x_cnt,y_cnt=0,0
            x,not_x='',''
            answer+=1
    if x:
        answer+=1
    return answer

s="abracadabra"
print(solution(s))
