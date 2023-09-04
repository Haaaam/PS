# 스택/큐
# 올바른 괄호


def solution(s):
    answer = True
    stack=list(s)
    cnt=0
    if stack[0]==")" or stack[-1]=="(":
        answer=False
    else:
        for i in stack:
            if i=="(":
                cnt+=1
            elif i==")":
                cnt-=1
            if cnt<0:
                answer=False
                break

        if cnt==0:
            answer=True
        else:
            answer=False

    return answer

s="()()()((())()()()()()"
stack=list(s)
answer=True


cnt=0
if stack[0]==")" or stack[-1]=="(":
    answer=False
else:
    for i in stack:
        if i=="(":
            cnt+=1
        elif i==")":
            cnt-=1
        if cnt<0:
            answer=False
            break
    if cnt==0:
        answer=True
    else:
        answer=False
print(answer)