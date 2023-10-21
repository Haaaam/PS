def solution(x,y,n):

    dp=[float('inf')]*1000001
    dp[x]=0

    if x==y:
        return 0

    for i in range(x,y+1):
        if dp[i]==float('inf'):
            continue

        if i+n<=y:
            dp[i+n]=min(dp[i+n],dp[i]+1)
        if i*2<=y:
            dp[i*2]=min(dp[i*2],dp[i]+1)
        if i*3<=y:
            dp[i*3]=min(dp[i*3],dp[i]+1)

    if dp[y]==float('inf'):
        return -1

    return dp[y]
# x를 y로 변환하려고 한다.
# x에 n을 더한다.
# x에 2를 곱한다.
# x에 3을 곱한다.
# x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return
# x를 y로 만들 수 없다면 -1을 return
#### 다이나믹 프로그래밍 방법으로 접근
# 다이나믹 프로그래밍 문제에서는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복된다.
# 분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않는다.

x,y,n=10,40,30
answer=0

dp=[float('inf')]* 1000001
dp[x]=0

# x랑 y가 같은 경우
if x==y:
    print(0)

for i in range(x,y+1):
    if dp[i]==float('inf'):
        continue
    if i+n<=y:
        dp[i+n]=min(dp[i+n],dp[i]+1)

    if i*2<=y:
        dp[i*2]=min(dp[i*2],dp[i]+1)
    if i*3<=y:
        dp[i*3]=min(dp[i*3],dp[i]+1)

if dp[y]==float('inf'):
    print( -1)



print(dp[y])