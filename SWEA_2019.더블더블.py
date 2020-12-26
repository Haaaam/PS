n=int(input())
res=1
for i in range(1,n+2):
    if i==1:
        print(res,end=' ')
    else:
        res*=2
        print(res,end=' ')
