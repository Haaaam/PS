res=0
for _ in range(int(input())):
    ans=list(input())
    stack=[]
    for i in ans:
        if len(stack)==0:
            stack.append(i)
        else:
            if stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
    if len(stack)==0:
        res+=1
print(res)

