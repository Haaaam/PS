n=int(input())

graph=[]
visited=[[False]*(n)for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0
res=[]
for i in range(n):
    graph.append(list(map(int,input())))
def dfs(x,y):
    global cnt
    cnt+=1
    visited[x][y]=True
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny]==1 and visited[nx][ny]==False:
                dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visited[i][j]==False:
            cnt=0
            dfs(i,j)
            res.append(cnt)
print(len(res))
res.sort()
for i in res:
    print(i)

