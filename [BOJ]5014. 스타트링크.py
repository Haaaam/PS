#2021.03.05
#[BOJ]5014. 스타트링크
from collections import deque
f,s,g,u,d=map(int,input().split())
visited=[0]*(f+1)
def bfs(f,s,g,u,d):
    queue=deque()
    queue.append((0,s))
    visited[s]=1
    while queue:
        cnt,target=queue.popleft()
        if target==g:
            return cnt
        if target+u<=f and visited[target+u]==0:
            visited[target+u]=1
            queue.append((cnt+1,target+u))
        if target-d>=1 and visited[target-d]==0:
            visited[target-d]=1
            queue.append((cnt+1,target-d))

    return "use the stairs"

print(bfs(f,s,g,u,d))

