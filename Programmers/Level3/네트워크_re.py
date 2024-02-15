# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때,
# 네트워크의 개수를 return
"""
제한사항
- 컴퓨터의 개수 n은 1이상 200이하인 자연수
- 각 컴퓨터는 0부터 n-1인 정수로 표현
- i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현
- computers[i][i]는 항상 1이다.
"""

def dfs(n,computers,v,visited):
    visited[v]=True

    for i in range(n):
        if i!=v and computers[v][i]==1:
            if not visited[i]:
                dfs(n,computers,i,visited)

def solution(n, computers):
    answer = 0
    # 각 노드의 방문 정보 기록
    visited=[False]*n
    for v in range(n):
        if not visited[v]:
            dfs(n,computers,v,visited)
            answer+=1

    return answer

n=3
computers=[[1,1,0],[1,1,0],[0,0,1]]

print(solution(n,computers))