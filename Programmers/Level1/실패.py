from collections import Counter
def solution(N, stages):
    user = len(stages)
    answer = {}
    stages = sorted(stages)

    for i in range(1, N + 1):
        if i in stages:
            answer[str(i)] = stages.count(i) / user
            user -= stages.count(i)
        else:
            answer[str(i)] = 0
    answer = sorted(answer.items(), key=lambda x: x[1], reverse=True)
    return [int(i[0]) for i in answer]


N=5
stages=[2,1,2,6,2,4,3,3]
# 실패율
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수/ 스테이지에 도달한 플레이어 수
# N: 스테이지의 개수, stages: 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return
user=len(stages)
answer={}
stages=sorted(stages)

for i in range(1,N+1):
    if i in stages:
        answer[str(i)]=stages.count(i)/user
        user-=stages.count(i)
    else:
        answer[str(i)]=0
answer=sorted(answer.items(), key=lambda x:x[1],reverse=True)
res=[int(i[0]) for i in answer]
print(res)