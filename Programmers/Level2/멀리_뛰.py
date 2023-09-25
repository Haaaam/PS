# 효진이는 멀리 뛰기를 연습중에 있다
# 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있다
# 다이나믹 프로그래밍
# 점화식: dp[n]=dp[n-1]+dp[n-2]


def solution(n):
    dp = [0] * 2001
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]%1234567

n=4
dp=[0]*2001
dp[1]=1
dp[2]=2
for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])