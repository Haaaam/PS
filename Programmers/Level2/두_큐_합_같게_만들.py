# 하나의 큐를 골라 원소를 추출하고, 추출된 원소를 다른 큐에 집어넣는 작업을 통해 각 큐의 원소 합이 같도록 만들려고 한다.
# 이때 필요한 작업의 최소 횟수를 구하고자 한다.
# 한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것으로 간주
# 큐는 먼저 집어넣은 원소가 먼저 나오는 구조
# return 각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수
# 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우 -1을 return
from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer=0

    # 두 수의 합이 같아질 수 없다면 -1을 return
    if (sum(queue1)+sum(queue2))%2!=0:
        return -1
    # 반복 가능 횟수에 제한 주기
    limit=len(queue1)*2+1
    # sum의 경우 O(n)의 복잡도를 갖기 때문에 변수로 선언해서 사용
    # while문 안에서 계속 sum()을 할 경우, 시간초과 남
    q1s,q2s=sum(queue1),sum(queue2)
    while q1s != q2s:
        if answer>limit:
            return -1
        if queue1 and q1s > q2s:
            a = queue1.popleft()
            queue2.append(a)
            q1s-=a
            q2s+=a
            answer += 1

        elif queue2 and q1s<q2s:
            a = queue2.popleft()
            queue1.append(a)
            q2s-=a
            q1s+=a
            answer += 1

    return answer



queue1=[3, 3, 3, 3]
queue2=[3, 3, 21, 3]

print(solution(queue1,queue2))