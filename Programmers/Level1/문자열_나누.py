def solution(s):
    answer = 0
    x = ''
    not_x = ''
    x_cnt = 0
    y_cnt = 0

    for i in range(len(s)):

        if not x:
            x += s[i]
            x_cnt += 1
        else:
            if s[i] == x[-1]:
                x += s[i]
                x_cnt += 1
            else:
                not_x += s[i]
                y_cnt += 1

            if x_cnt == y_cnt:
                answer += 1
                y_cnt, x_cnt = 0, 0
                x, not_x = '', ''

    if x:
        answer += 1
    return answer

# 첫글자 x
# x와 x가 아닌 다른 글자들이 나온 횟수를 세기
# 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리
#
s="aaabbaccccabba"
stack=[]

answer=0
x=''
not_x=''
x_cnt=0
y_cnt=0
for i in range(len(s)):

    if not x:
        x+=s[i]
        x_cnt+=1
    else:
        if s[i]==x[-1]:
            x+=s[i]
            x_cnt+=1
        else:
            not_x+=s[i]
            y_cnt+=1

        if x_cnt==y_cnt:
            answer+=1
            y_cnt,x_cnt=0,0
            x,not_x='',''

if x:
    answer+=1

print(answer)