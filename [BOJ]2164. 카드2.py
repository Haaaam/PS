from collections import deque
n=int(input())
card=deque([i for i in range(1,n+1)])
array=[]
while len(card)>1:
    if card:
        card.popleft()
        array.append(card.popleft())
        card.append(array.pop())
    else:
        break
print(*card)

