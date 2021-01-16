n=int(input())
t=list(map(int,input().split()))
t.sort(reverse=True)
res=0
for i,j in enumerate(t):
    res=max(res,i+j+2)
print(res)




