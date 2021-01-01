n=int(input())
a=list(map(int,input().split()))
stack=[] #stack에 index 삽입
res=[-1 for _ in range(n)]
for i in range(n):
    try:
        while a[stack[-1]]<a[i]:
            res[stack.pop()]=a[i]
    except:
        pass
    stack.append(i)
for i in range(n):
    print(res[i], end=' ')
