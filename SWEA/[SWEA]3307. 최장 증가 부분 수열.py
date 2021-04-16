#2021.02.10
#[SWEA]3307. 최장 증가 부분 수열

for i in range(int(input())):
    n,A=int(input()),list(map(int,input().split()))
    dp=[0]*1001
    for j in range(n):
        dp[j]=1
        for k in range(j):
            if A[k]<A[j]:
                dp[j]=max(dp[j],dp[k]+1)
    print(f"#{i+1} {max(dp)}")


