from collections import deque

n,k=map(int,input().split())
visited=[0]*100001

def bfs():
    queue=deque([n])
    while queue:
        x=queue.popleft()
        if x==k:
            return visited[x]
        location=[x-1,x+1,2*x]
        for l in location:
            if 0<=l<100001 and visited[l]==0:
                if l==2*x and x!=0 :
                    visited[l]=visited[x]
                    queue.appendleft(l)
                else:
                    visited[l]=visited[x]+1
                    queue.append(l)

print(bfs())


