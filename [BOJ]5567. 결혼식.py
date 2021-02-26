#2021.02.24
#[BOJ]5567. 결혼식
from collections import deque

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
friend=[10000 for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt=0
def bfs(v):
    queue=deque([v])
    friend[v]=0
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if friend[i]>friend[v]:
                friend[i]=friend[v]+1
                queue.append(i)

bfs(1)
cnt=0
for i in range(1,n+1):
    if friend[i]==1 or friend[i]==2:
        cnt+=1
print(cnt)
