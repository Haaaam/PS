n=int(input())
level=[]
for i in range(n):
    level.append(int(input()))
res=0
for i in range(n-1,0,-1):
    if level[i-1]>=level[i]:
        res+=level[i-1]-(level[i]-1)
        level[i-1]=level[i]-1
print(res)

