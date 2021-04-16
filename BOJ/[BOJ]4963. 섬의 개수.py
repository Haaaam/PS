#런타임 에러 방지
import sys
sys.setrecursionlimit(1000000000)

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

def dfs(x,y):
    visited[x][y]=True
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=h or nx<0 or ny>=w or ny<0:
            continue
        if graph[nx][ny]==1 and visited[nx][ny]==False:
            dfs(nx,ny)

while True:
    graph=[]
    cnt = 0
    w,h=map(int,input().split())
    visited = [[False] * (w) for _ in range(h)]
    if w==0 and h==0:
        break
    for i in range(h):
        graph.append(list(map(int,input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and visited[i][j]==False:
                dfs(i,j)
                cnt+=1
    print(cnt)


