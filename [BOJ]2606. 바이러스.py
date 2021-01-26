computer=int(input())
network=int(input())
visited=[False]*(computer+1)
graph=[[0]*(computer+1) for i in range(computer+1)]
virus=[]
def dfs(graph,v,visited):
    visited[v]=True
    virus.append(v)
    for i in range(1,computer+1):
        if visited[i]==0 and graph[v][i]==1:
            dfs(graph,i,visited)
    return len(virus)-1
for i in range(network):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1

print(dfs(graph,1,visited))




