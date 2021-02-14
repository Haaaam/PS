#2021.02.14
#[BOJ]1715. 카드 정렬하기
import heapq
n=int(input())
card=[]
res=0
for i in range(n):
    heapq.heappush(card,int(input()))
while len(card)>1:
    x,y=heapq.heappop(card),heapq.heappop(card)
    s=x+y
    res+=s
    heapq.heappush(card,s)
print(res)


