#2021.02.11
#[BOJ]1303. 전쟁 - 전투
from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
w,b=0,0

graph=[list(input()) for _ in range(m)]
visited=[[False]*n for i in range(m)]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    cnt=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny]==graph[x][y] and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    queue.append((nx,ny))
                    cnt+=1

    return cnt

for i in range(m):
    for j in range(n):
        if visited[i][j]==False:
            count=bfs(i,j)
            if graph[i][j]=='W':
                w+=count**2
            else:
                b+=count**2
print(w,b)


