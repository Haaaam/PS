# 완전탐색
# 일부 테스트 케이스 통과 못함
"""
def solution(k,dungeons):
    answer = 0
    stack = [dungeons[0]]

    for idx in range(1, len(dungeons)):
        pre_a, pre_b = dungeons[idx - 1]
        a, b = dungeons[idx]
        if pre_b > a:
            tmp = stack.pop()
            stack.append(dungeons[idx])
            stack.append(tmp)
        else:
            stack.append(dungeons[idx])
    for idx in stack:
        a, b = idx
        if k >= a:
            k -= b
            answer += 1
    return answer


def solution(k,dungeons):
    answer=0
    dungeons=sorted(dungeons, key=lambda x:x[0]-x[1],reverse=True)
    for idx in dungeons:
        a, b = idx

        if k >= a:
            k -= b
            answer += 1

    return answer
"""

# 피로도 시스템이 있으며, 일정 피로도를 사용해서 던전을 탐험할 수 있다.
# 던전마다 탐험을 시작하기 위해 필요한 "최소 필요도"
# 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"
# "최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도
# k: 현재 피로도
# dungeons: ["최소 필요 피로도", "소모 피로도"]
# return 유저가 탐험할 수 있는 최대 던전 수

answer=0
def dfs(k,v,dungeons,visited):
    global answer
    answer=max(answer,v)
    for i in range(len(dungeons)):
        if visited[i]==0 and k>=dungeons[i][0] :
            visited[i]=1
            dfs(k-dungeons[i][1],v+1,dungeons,visited)
            visited[i]=0

def solution(k,dungeons):
    visited=[0]*len(dungeons)
    dfs(k,0,dungeons,visited)
    return answer

k=80
dungeons=[[80,20],[50,40],[30,10]]

print(solution(k,dungeons))

