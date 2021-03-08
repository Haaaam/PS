#2021.03.09
#[BOJ]16948. 데스 나이트

from collections import deque

n=int(input())
r1,c1,r2,c2=map(int,input().split())
dx,dy=[-2,-2,0,0,2,2],[-1,1,-2,2,-1,1]
graph=[[0]*n for _ in range(n)]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        if x == r2 and y == c2:
            return graph[x][y]

        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==0:
                    graph[nx][ny]=graph[x][y]+1
                    queue.append((nx,ny))
    else:
        return -1

print(bfs(r1,c1))








