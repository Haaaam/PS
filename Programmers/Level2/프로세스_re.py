# 1. 실행 대기 큐에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣는다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다. -> 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
# 숫자가 클수록 우선순위가 높다.
# priorities: 프로세스의 중요도가 순서대로 담긴 배열
# location: 몇 번째로 실행되는지 알고싶은 프로세스의 위치
# 해당 프로세스가 몇 번째로 실행되는지 return
from collections import deque
def solution(priorities,location):
    answer=0
    queue=deque(priorities)

    # 우선순위가 있을때까지 계속 실행
    while queue:
        first=max(queue)
        pop=queue.popleft()
        location-=1

        if pop!=first:
            if location<0:
                location=len(queue)-1
        else:
            answer+=1
            if location<0:
                return answer
    return answer

priorities=[2,1,3,2]
location=2
print(solution(priorities,location))