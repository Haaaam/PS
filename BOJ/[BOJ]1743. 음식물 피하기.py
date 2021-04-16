from collections import deque
#n:세로의 길이, m: 가로의 길이, k:음식물 쓰레기의 수
n,m,k=map(int,input().split())

visited=[[False]*m for _ in range(n)]
graph=[[0]*m for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    cnt=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False :
                if graph[nx][ny]==1 :
                    visited[nx][ny]=True
                    cnt+=1
                    queue.append((nx,ny))
    return cnt

res=0
for i in range(k):
    r,c=map(int,input().split())
    graph[r-1][c-1]=1

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            res=max(res,bfs(i,j))

print(res)

