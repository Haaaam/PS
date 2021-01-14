n,k=map(int,input().split())
num=list(input())
stack=[]
a=k
for i in range(n):
    while a>0 and stack:
        if stack[-1]<num[i]:
            stack.pop()
            a-=1
        else:
            break
    stack.append(num[i])
print(''.join(stack[:n-k]))