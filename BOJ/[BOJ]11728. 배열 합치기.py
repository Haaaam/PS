n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=[i for i in a]+[i for i in b]
res.sort()
print(*res)