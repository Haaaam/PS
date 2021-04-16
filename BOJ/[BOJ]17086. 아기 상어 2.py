#2021.02.16
#[BOJ]17086. 아기 상어 2
from collections import deque
n,m=map(int,input().split())
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]

graph=[]
queue=deque()
def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0:
                    graph[nx][ny]=graph[x][y]+1
                    queue.append((nx,ny))

for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j]:
            queue.append((i,j))
bfs()
print(max(map(max,graph))-1)



'''from collections import deque
n,m=map(int,input().split())
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]

graph=[]

def bfs(x,y):
    queue=deque()
    queue.append((x,y,0))
    visited[x][y]=True
    while queue:
        x,y,cnt=queue.popleft()
        if graph[x][y]==1:
            return cnt
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==False:
                    visited[nx][ny]=True
                    queue.append((nx,ny,cnt+1))
    return 0


for i in range(n):
    graph.append(list(map(int,input().split())))
res=0
for i in range(n):
    for j in range(m):
        visited = [[False] * m for _ in range(n)]
        ans=bfs(i,j)
        if ans>res:
            res=ans
print(res)'''