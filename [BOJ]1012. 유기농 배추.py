from collections import deque
t=int(input())
#m:가로길이, n:세로길이, k:배추가 심어져 있는 위치의 개수
dx=[-1,1,0,0]
dy=[0,0,-1,1]
res=[]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

for i in range(t):
    m,n,k=map(int,input().split())
    graph = [[0] * n for _ in range(m)]

    for j in range(k):
        a,b=map(int,input().split())
        graph[a][b]=1

    cnt=0
    for x in range(m):
        for y in range(n):
            if graph[x][y]==1:
                bfs(x,y)
                cnt+=1
    res.append(cnt)
for i in res:
    print(i)

