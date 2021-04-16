from itertools import combinations
import sys
n,m=map(int,input().split())

chicken,house=[],[]
for i in range(n):
    graph=list(map(int,input().split()))
    for j in range(n):
        if graph[j]==1:
            house.append((i,j))
        elif graph[j]==2:
            chicken.append((i,j))
comb=list(combinations(chicken,m))

def sol(comb):
    res=0
    for i,j in house:
        tmp=sys.maxsize
        for x,y in comb:
            tmp=min(tmp,abs(i-x)+abs(j-y))
        res+=tmp
    return res
res=sys.maxsize
for c in comb:
    res=min(res,sol(c))
print(res)

