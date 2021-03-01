#2021.03.01
#[BOJ]3184. 양

r,c=map(int,input().split())
graph=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(r):
    graph.append(list(input()))

def bfs(x,y):
    queue=[(x,y)]
    wolf,sheep=0,0
    while queue:
        x,y=queue.pop()
        if graph[x][y]=='v':
            wolf+=1
        if graph[x][y]=='o':
            sheep+=1
        graph[x][y]='#'

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]

            if 0<=nx<r and 0<=ny<c:
                if graph[nx][ny]!='#':
                    queue.append((nx,ny))
    if sheep>wolf:
        wolf=0
    else:
        sheep=0
    return sheep,wolf

sheep,wolf=0,0
for i in range(r):
    for j in range(c):
        if graph[i][j]=='v' or graph[i][j]=='o':
            s,w=bfs(i,j)
            sheep+=s
            wolf+=w

print(sheep,wolf)










