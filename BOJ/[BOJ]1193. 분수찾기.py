n=int(input())
cnt=0
while n>0:
    n-=cnt
    cnt+=1
n=cnt+n-1
res=str(n)+'/'+str(cnt-n)
if cnt%2==0:
    res=str(cnt-n)+'/'+str(n)
print(res)
