n=int(input())
data=list(map(int,input().split()))
res=[]

for i in range(n):
    res.insert(data[n-1-i],n-i)
print(*res)

