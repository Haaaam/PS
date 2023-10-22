def solution(n):
    dp = [0] * 60001

    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    return dp[n]


# 가로 길이가 2이고 세로의 길이가 1인 직사각형모양의 타일이 있다.
# 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우려고 한다.
# 직사각형의 가로의 길이 n이 매개변수로 주어질 때, 이 직사각형을 채우는 방법의 수를 return

n=4
dp=[0]*60001

dp[1]=1
dp[2]=2
for i in range(3,n+1):
    dp[i]=(dp[i-1]+dp[i-2])%1000000007
print(dp[n])