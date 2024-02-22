# 영어 단어가 적힌 카드 뭉치 두 개
# 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용한다.
# 한 번 사용한 카드는 다시 사용할 수 없다.
# 카드를 사용하지 않고 다음 카드로 넘어갈 수 없다.
# 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.

# deque로 접근
# answer과 check변수를 만들어 goal에 있는 카드를 cards1과 cards2에서 순서대로 꺼냈을때
# 만족하는지 확인
# answer이 정답, check는 cards1&cards2의 카드를 순서대로 꺼냈을 때 정답이 완성되는지 확인용
"""
from collections import deque
def solution(cards1, cards2, goal):
    answer,check='',''
    cards1,cards2=deque(cards1),deque(cards2)
    for i in range(len(goal)):
        a=goal[i]
        answer+=goal[i]
        if a in cards1 and len(cards1)>0:
            b=cards1.popleft()
            check+=b
        elif a in cards2 and len(cards2)>0:
            b=cards2.popleft()
            check+=b

    if answer==check:
        return "Yes"
    else:
        return "No"
"""

# 다른 사람 풀이
def solution(cards1, cards2, goal):
    for i in goal:
        if len(cards1)>0 and i==cards1[0]:
            cards1.pop(0)
        elif len(cards2)>0 and i==cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
cards1=["i", "water", "drink"]
cards2=["want", "to"]
goal=["i","want","to","drink","water"]
print(solution(cards1,cards2,goal))