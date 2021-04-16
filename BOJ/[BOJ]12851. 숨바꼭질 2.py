from collections import deque

n,k=map(int,input().split())
visited=[False]*100001
graph=[0]*100001
cnt=[0]*100001
def bfs():
    queue=deque([n])
    visited[n]=True
    cnt[n]=1
    while queue:
        x=queue.popleft()
        location=[x-1,x+1,x*2]
        for l in location:
            if 0<=l<=100000:
                if visited[l]==False:
                    visited[l]=True
                    graph[l]=graph[x]+1
                    cnt[l]=cnt[x]
                    queue.append(l)
                elif graph[l]==graph[x]+1:
                    cnt[l]+=cnt[x]

bfs()
print(graph[k])
print(cnt[k])


