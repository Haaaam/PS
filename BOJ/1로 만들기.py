# 1로 만들기
# 횟수 구하기



x=10


dp=[0]*1000001

for i in range(2,x+1):
    # 1로 뺀 경우
    dp[i]=dp[i-1]+1

    if i%3==0:
        dp[i]=min(dp[i//3]+1,dp[i])

    if i%2==0:
        dp[i]=min(dp[i//2]+1,dp[i])


print(dp[x])