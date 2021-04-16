r,c=map(int,input().split())
graph=[list(input()) for _ in range(r)]
cnt=1
dx,dy=[-1,1,0,0],[0,0,-1,1]
def bfs(x,y):
    global cnt
    queue=set()
    queue.add((x,y,graph[x][y]))
    while queue:
        x,y,next=queue.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and graph[nx][ny] not in next:
                queue.add((nx,ny,next+graph[nx][ny]))
                cnt=max(cnt,len(next)+1)
bfs(0,0)
print(cnt)

