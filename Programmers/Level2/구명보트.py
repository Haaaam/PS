from collections import deque

def solution(people, limit):
    res = 0
    people.sort()
    queue = deque(people)

    while len(queue) > 0:
        if len(queue) == 1:
            res += 1
            queue.pop()
            break
        if queue[0] + queue[-1] > limit:
            queue.pop()
            res += 1
        else:
            queue.popleft()
            queue.pop()
            res += 1

    return res

people=[70,50,80,50]
limit=100
people=sorted(people)

queue=deque(people)
res=0

while len(queue)>0:
    # 한명 일때
    if len(queue)==1:
        res+=1
        queue.pop()
        break
    # 두명 이상일때
    if queue[0]+queue[-1]>limit:
        queue.pop()
        res+=1
    else:
        queue.popleft()
        queue.pop()
        res+=1



print(res)