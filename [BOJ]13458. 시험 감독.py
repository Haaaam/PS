n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
res=0
for i in range(len(a)):
    if a[i]>0:
        a[i]-=b
        res+=1
    if a[i]>0:
        res+=int(a[i]/c)
        if a[i]%c!=0:
            res+=1
print(int(res))



