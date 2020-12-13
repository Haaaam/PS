a,b=map(int,input().split())
n=max(a,b)-min(a,b)
s=(n*(n+1))//2
print(s+min(a,b)*(n+1))
