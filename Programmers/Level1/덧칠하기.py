def solution(n,m,section):
    answer = 0

    paint = section[0]-1

    for i in section:
        if paint < i:
            paint = i + m - 1

            answer += 1

    return answer
# 벽 전체에 페인트를 새로 칠하는 대신, 구역을 나누어 일부만 페인트를 새로 칠 함으로써 예산을 아끼려 한다.
# 벽을 1미터 길이의 구역 n개로 나누고, 각 구역에 왼쪽부터 순서대로 1번부터 n번까지 번호를 붙이기
# 페인트를 다시 칠해야 할 구역들 정하기
# 페인트를 칠하는 롤러의 길이는 m미터, 롤러로 벽에 페인트를 한 번 칠하는 규칙
# 롤러가 벽에서 벗어나면 안된다
# 구역의 일부분만 포함되도록 칠하면 안된다.

# n: 벽을 1미터 길이의 구역으로 나눈 갯수
# m: 페인트 칠하는 롤러의 길이
n,m=map(int,input().split())
section=list(map(int,input().split()))
# return 롤러로 페인트칠해야하는 최소 횟수
answer=0

paint=section[0]-1 # 처음 페인트 칠 해야하는 위치


for i in section:

    if paint<i:
        paint=i+m-1 # 페인트칠 벽 영역 갯수 1개 빼줘야 함
        answer+=1



print(answer)
