import sys
input=sys.stdin.readline

n=int(input())
a=[0]+list(map(int,input().split()))

for i in range(1,n+1):
    a[i]+=a[i-1]

m=int(input())

for i in range(m):

    x,y=map(int,input().split())
    print(a[y]-a[x-1])

