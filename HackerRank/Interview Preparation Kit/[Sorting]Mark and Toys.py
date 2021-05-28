n,k=map(int,input().split())
prices=sorted(list(map(int,input().split())))
res,cnt=0,0
for i in prices:
    if res+i<=k:
        res+=i
        cnt+=1
    else:
        break
print(cnt)
