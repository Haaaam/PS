#2021.02.23
#[BOJ]11053. 가장 긴 증가하는 부분 수열

n=int(input())
dp=[0]*(n+1)
num=list(map(int,input().split()))

for i in range(n):
    dp[i]=1
    for j in range(i):
        if num[i]>num[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
