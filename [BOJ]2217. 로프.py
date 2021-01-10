n=int(input())
m=[]
res=0
for i in range(n):
    m.append(int(input()))
m.sort()
for i in range(n-1,-1,-1):
    m[i]=m[i]*(n-i)
    if res<m[i]:
        res=m[i]
print(res)

