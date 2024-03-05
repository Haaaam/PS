# 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어 있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때
# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return

def dfs(n,visited,computers,v):
    visited[v]=True
    for i in range(n):
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if i!=v and computers[v][i]==1:
            if not visited[i]:
                dfs(n,visited,computers,i)

def solution(n, computers):
    answer = 0
    visited=[False]*n
    for v in range(n):
        # v번째 노드를 방문하지 않았을 경우
        if not visited[v]:
            # 정의된 dfs 함수 호출
            dfs(n,visited,computers,v)
            answer+=1

    return answer

n=3
computers=[[1,1,0],[1,1,0],[0,0,1]]
print(solution(n,computers))