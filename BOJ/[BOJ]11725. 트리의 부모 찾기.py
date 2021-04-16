#2021.02.24

import sys
sys.setrecursionlimit(100000)

n=int(input())
graph=[[] for _ in range(n+1)]

parent=[0 for _ in range(n+1)]
parent[1]=1

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    for i in graph[v]:
        if parent[i]==0:
            parent[i]=v
            dfs(i)
dfs(1)
for i in parent[2:]:
    print(i)



