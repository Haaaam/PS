# 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 한다.
# emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return
def solution(emergency):
    answer=[]
    emergency_e = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(emergency_e.index(i) + 1)

    return answer

emergency=[3,76,24]

print(solution(emergency))