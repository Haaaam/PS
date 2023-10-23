from collections import deque
# 최단거리 구하는 문제는 bfs로 접근
# dfs는 13초 까지 시간이 주어지는 경우만 가능?
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(x,y,maps):
    global n,m
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1:
                queue.append((nx,ny))
                maps[nx][ny]=maps[x][y]+1
    if maps[n-1][m-1]==1:
        return -1
    return maps[n-1][m-1]

def solution(maps):
    global n,m
    n,m=len(maps),len(maps[0])
    answer=bfs(0,0,maps)

    return answer

# 상대팀 진영에 도착할 수 없을 때는 -1 입력
# 상대팀 진영은 우측 하단인 n,m 위치에 있다.

maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

print(solution(maps))
