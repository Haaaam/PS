tc=int(input())
for t in range(tc):
    n=int(input())
    dp=[0]*n
    num=list(map(int,input().split()))
    dp[0]=num[0]
    res=0
    for i in range(1,n+1):
        dp[i]=max(dp[i-1]+num[i],num[i])

    print(f"#{t+1} {max(dp)}")