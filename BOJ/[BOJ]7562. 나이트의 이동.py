from collections import deque

t=int(input())#테스트 케이스의 개수
dx=[1,1,2,2,-1,-1,-2,-2]
dy=[2,-2,1,-1,2,-2,1,-1]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        if x==c and y==d:
            return graph[x][y]
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<l and 0<=ny<l:
                if graph[nx][ny]==0:
                    graph[nx][ny]=graph[x][y]+1
                    queue.append((nx,ny))

for i in range(t):
    l=int(input())
    graph=[[0]*l for _ in range(l)]
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    print(bfs(a,b))

    