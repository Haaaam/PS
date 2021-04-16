#2021.03.08
#[BOJ]2589. 보물섬
from collections import deque
r,c=map(int,input().split())
graph=[list(input()) for _ in range(r)]

dx,dy=[-1,1,0,0],[0,0,-1,1]
res=[]

def bfs(x,y):
    cnt=0
    queue=deque()
    queue.append((x,y))
    visited = [[0] * c for _ in range(r)]
    visited[x][y]=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<r and 0<=ny<c:
                if graph[nx][ny]=='L' and visited[nx][ny]==0:
                    visited[nx][ny]=visited[x][y]+1
                    queue.append((nx, ny))
                    cnt=max(cnt,visited[nx][ny])

    res.append(cnt-1)


for i in range(r):
    for j in range(c):
        if graph[i][j]=='L':
            bfs(i,j)
print(max(res))


