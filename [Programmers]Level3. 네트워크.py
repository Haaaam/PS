n=3
computers=[[1,1,0],[1,1,1],[0,1,1]]


def solution(n,computers):
    answer=0
    visited =[False]*n
    def dfs(visited,computers,v):
        visited[v]=True
        for i in computers[v]:
            if not visited[i]:
                dfs(visited,computers,i)
    for i in range(n):
        if not visited[i]:
            dfs(visited,computers,)
            answer+=1
    return answer



