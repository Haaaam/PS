from collections import deque
def solution(priorities, location):
    answer = 0  # 순서
    queue = deque(priorities)
    while queue:
        # 우선순위가 가장 높은 것
        top=max(queue)
        pop=queue.popleft()
        location-=1

        if top!=pop:
            queue.append(pop)
            if location<0:
                location=len(queue)-1

        else:
            answer += 1
            if location<0:
                return answer



# 실행 대기 큐에서 대기중인 프로세스 하나를 꺼냅니다.
# 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣는다.
# 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행한다.
 # 한번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료

# 프로세스 [A,B,C,D]
priorities=[1, 1, 9, 1, 1, 1]
location=0
print(solution(priorities,location))
