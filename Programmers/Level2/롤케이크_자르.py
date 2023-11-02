from collections import Counter
def solution(topping):
    a, b = set(), Counter(topping)

    answer = 0
    for t in topping:
        b[t] -= 1  # 동생이 가지고 있는 토핑 제거
        if b[t]==0:
            del b[t]
        # 철수 케이크에 토핑이 존재하지 않을 경우
        if t not in a:
            a.add(t)

        if len(a) == len(b):
            answer += 1
    return answer


# 시간초과
"""
    answer = 0

    for i in range(1, len(topping)):
        tmp_1, tmp_2 = topping[:i], topping[i:]
        if len(set(tmp_1)) == len(set(tmp_2)):
            answer += 1
    return answer
"""
# 철수는 롤케이크를 두조각으로 잘라서 동생과 한조각씩 나눠 먹으려고 한다.
# 롤케이크 토핑이 중요. 동일한 가짓수의 토핑이 올라가면 공평하게 나누어진 것으로 생각
# return topping이 매개변수로 주어질 때, 롤케이크를 자르는 방법의 수를 return
# 롤케이크를 공평하게 나눌 수 없는 경우도 생각하기

topping=[1, 2, 3, 1, 4]
a,b=set(),Counter(topping)
answer=0
for t in topping:
    b[t]-=1# 동생이 가지고 있는 토핑 제거
    if b[t]==0:
        del b[t]
    # 철수 케이크에 토핑이 존재하지 않을 경우
    if t not in a:
        a.add(t)

    if len(a)==len(b):
        answer+=1
print(answer)