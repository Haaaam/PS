from collections import deque
n,k=map(int,input().split())
visited=[0]*100001

def bfs():
    queue=deque([n])
    visited[n]=0
    while queue:
        x=queue.popleft()
        if x==k:
            print(visited[x])
            break
        location=[x-1,x+1,x*2]
        for l in location:
            if 0<=l<=100000 and visited[l]==0:
                visited[l]=visited[x]+1
                queue.append(l)
bfs()

