#2021.02.15
#[BOJ]2583. 영역 구하기

from collections import deque
m,n,k=map(int,input().split())
graph=[[0]*(n) for _ in range(m)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    graph[x][y]=1
    cnt=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny]==0:
                    graph[nx][ny]=1
                    cnt += 1
                    queue.append((nx,ny))

    return cnt

for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for j in range(y1, y2):
        for i in range(x1,x2):
            graph[j][i]=1


res=[]
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            res.append(bfs(i,j))
print(len(res))
res.sort()
print(*res)



