import sys
sys.setrecursionlimit(1000000000)
n=int(input())
graph=[]
visited=[[False]*n for _ in range(n)]

cnt1=0#정상인
cnt2=0#적록색약

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    visited[x][y]=True
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if visited[nx][ny]==False and graph[x][y]==graph[nx][ny]:
                dfs(nx,ny)

for i in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            cnt1+=1
            dfs(i,j)

for i in range(n):
    for j in range(n):
        if graph[i][j]=='G':
            graph[i][j]='R'

#위에서 dfs를 돌면서 방문한 노드들을 True로 변경 했기때문에
#적록색약인 사람이 봤을 때의 구역을 구하기위해 다시 False로 초기화 해준다.
visited=[[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            cnt2+=1
            dfs(i,j)
print(cnt1,cnt2)



