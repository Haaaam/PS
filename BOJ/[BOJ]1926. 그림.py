from collections import deque
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

dx,dy=[-1,1,0,0],[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    graph[x][y]=0
    size=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                size+=1
                queue.append((nx,ny))
    else:
        res.append(size)
        return

cnt=0
res=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            bfs(i,j)
            cnt+=1
print(cnt)
if len(res)==0:
    print(0)
else:
    print(max(res))