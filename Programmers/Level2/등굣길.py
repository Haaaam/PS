# dp로 접근
def solution(m,n,puddles):
    # puddles 행,열 위치 바꿔줘야 함
    puddles=[[q,p] for [p,q] in puddles]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # 집의 위치(시작 위치)

    # 물이 잠긴 지역 -1로 표현

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if i == 1 and j == 1:
                continue
            # 장애물은 1개만 있지 않음!!
            if [i,j] in puddles:
                dp[i][j] = 0  # 물이 잠긴 지역 -1로 표현
            else:
                # 점화식: 현재위치에서 왼쪽과 위쪽의 합이 현재 값이 되게 한다.
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000007
    return dp[n][m]

# 물에 잠기지 않은 지역을 통해 학교를 가려고 한다.
# 집에서 학교까지 가는 길은 mxn 크기의 격자모양

# 격자 크기 m,n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles 매개변수 주어진다.
# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수
m,n=4,3
puddles=[[2,2]] # 물이 잠긴 지역
answer=0
dp=[[0]*(m+1) for i in range(n+1)]
dp[1][1]=1 # 집의 위치(시작 위치)

# 물이 잠긴 지역 -1로 표현

for i in range(1,n+1):
    for j in range(1,m+1):

        if i==1 and j==1:
            continue
        if [i,j] in puddles:
            dp[i][j]=0 # 물이 잠긴 지역 -1로 표현
        else:
            dp[i][j]=(dp[i][j-1]+dp[i-1][j])
print(dp[n][m])