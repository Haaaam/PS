def dfs(n,visited,computers,computer):
        visited[computer]=True
        for i in range(n):
            if i!=computer and computers[computer][i]==1:
                if not visited[i]:
                    dfs(n,visited,computers,i)
                    
def solution(n,computers):
    answer=0
    visited =[False]*n
    for computer in range(n):
        if not visited[computer]:
            dfs(n,visited,computers,computer)
            answer+=1
    return answer


