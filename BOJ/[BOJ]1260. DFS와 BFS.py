from collections import deque
def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    for i in range(1,n+1):
        if visited[i]==0 and graph[v][i]==1:
            dfs(graph,i,visited)
def bfs(graph,v,visited):
    queue=deque([v])
    visited[v]=False
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if visited[i]==1 and graph[v][i]==1:
                queue.append(i)
                visited[i]=False



n,m,v=map(int,input().split())
visited=[False]*(n+1)
graph=[[0]*(n+1) for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1
dfs(graph,v,visited)
print()
bfs(graph,v,visited)

