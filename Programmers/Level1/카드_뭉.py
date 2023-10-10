from collections import deque
def solution(cards1, cards2, goal):

    real, check = '', ''
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for idx in range(len(goal)):
        real += goal[idx]

        if goal[idx] in cards1 and len(cards1) > 0:
            a = cards1.popleft()
            check += a
        elif goal[idx] in cards2 and len(cards2) > 0:
            a = cards2.popleft()
            check += a

    if check == real:
        return "Yes"
    else:
        return "No"


# 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용
# 한번 사용한 카드는 다시 사용 불가
# 카드를 사용하지 않고 다음 카드로 넘어가기 불가
# 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없다

# return cards1과 cards2에 적힌 단어들로 goal을 만들 수 있다면 "Yes", 만들 수 없다면 "No"

cards1,cards2=["i", "water", "drink"],["want", "to"]
cards1=deque(cards1)
cards2=deque(cards2)

goal=["i", "want", "to", "drink", "water"]
answer=''
real,check='',''
for idx in range(len(goal)):
    real+=goal[idx]

    if goal[idx] in cards1 and len(cards1)>0:
        a=cards1.popleft()
        check+=a
    elif goal[idx] in cards2 and len(cards2)>0:
        a = cards2.popleft()
        check+=a

if check==real:
    answer="Yes"
else:
    answer="No"
print(answer)