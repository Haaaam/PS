#n:수의 개수, m:합을 구해야 하는 횟수
import sys

n,m=map(int,input().split())
l=list(map(int,sys.stdin.readline().split()))
res=[0 for _ in range(n)]
for i in range(n):
    if i==0:
        res[i]=l[i]
    else:
        res[i]=res[i-1]+l[i]
for k in range(m):
    i,j=map(int,sys.stdin.readline().split())
    if i==1:
        print(res[j-1])
    else:
        print(res[j-1]-res[i-2])



