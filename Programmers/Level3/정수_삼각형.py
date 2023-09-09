def solution(triangle):
    answer = 0
    return answer

# 아래 칸으로 이동할 때는 대각선 방향
# 한 칸 오른쪽 또는 왼쪽으로만 이동 가능

triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
dp=triangle
for i in range(1,len(triangle)):
    print("i:",i)

    for j in range(i+1):
        # 위에서 왼쪽 아래로 내려간 경우
        if j==0:
            up_left=0
        else:
            up_left = triangle[i-1][j-1]
        # 바로 위에서 내려온 경우
        if j == i:
            up = 0
        else:
            up = triangle[i-1][j]
        dp[i][j]=dp[i][j]+max(up_left,up)
print(max(dp[len(triangle)-1]))
