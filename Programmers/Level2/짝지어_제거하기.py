def solution(s):
    stack = [s[0]]
    answer = 1
    for i in range(1, len(s)):

        if stack:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
        if len(stack)!=0:
            answer=0

    return answer

s="baabaa"
stack=[s[0]]
answer=1
for i in range(1,len(s)):

    if stack:
        if stack[-1]==s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    else:
        stack.append(s[i])
if len(stack)!=0:
    answer=0
print(answer)

