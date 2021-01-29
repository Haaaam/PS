from collections import deque
n=int(input())
a,b=map(int,input().split())
m=int(input())
graph=[[]for _ in range(n+1)]
visited=[False]*(n+1)

def bfs(graph,v,visited):
    queue=deque([v])
    visited[v]=True
    cnt=0
    while queue:
        cnt+=1
        for _ in range(len(queue)):
            v=queue.popleft()
            if v==b:
                return cnt-1
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i]=True
    return -1


for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
print(bfs(graph,a,visited))
