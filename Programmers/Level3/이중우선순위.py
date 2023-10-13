# 이중우선순위큐

def solution(operations):

    answer = []
    for i in range(len(operations)):
        a, b = operations[i].split(' ')
        b = int(b)
        if a == "I":
            answer.append(b)
        elif a == "D":
            if b == -1 and answer:
                answer.remove(min(answer))
            elif b != -1 and answer:
                answer.remove(max(answer))
        print(answer)
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0, 0]


# I 숫자: 큐에 주어진 숫자를 삽입합니다.
# D 1: 큐에서 최댓값을 삭제합니다.
# D-1: 큐에서 최솟값을 삭제합니다.

# Operations 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]

operations=["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
answer=[]
for i in range(len(operations)):
    a,b=operations[i].split(' ')
    b=int(b)
    if a=="I":
        answer.append(b)
    elif a=="D":
        if b==-1 and answer:
            answer.remove(min(answer))
        elif b!=-1 and answer:
            answer.remove(max(answer))
    print(answer)
if answer:
    print([max(answer),min(answer)])
else:
    print([0,0])



