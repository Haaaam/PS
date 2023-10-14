# heapq 사용
import heapq

def solution(n, works):
    if n >= sum(works):
        return 0
    else:
        # heapq로 변환
        heapq.heapify(works)
        max_works = []
        # heapq로 변환한 works에서 최대heap을 구하기 위한 방법

        for i in works:
            heapq.heappush(max_works, (-i, i))

        for i in range(n):
            max_ = heapq.heappop(max_works)[1]
            max_ -= 1
            heapq.heappush(max_works, (-max_, max_))


    return sum(i[1] ** 2 for i in max_works)

### 어차피 제곱을 하기때문에 works의 값들을 -로 변환하여 heapq로 만들어서 구해도 됨됨

works[2,1,2]
n=1
answer=0
heapq.heapify(works)
max_works=[]
for i in works:
    heapq.heappush(max_works,(-i,i))

for i in range(n):
    max_=heapq.heappop(max_works)[1]
    max_-=1
    heapq.heappush(max_works,(-max_,max_))
print(sum(i[1]**2 for i in max_works))
# works에 대해 야근 피로도를 최소화한 값을 리턴
# 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값
# n시간 동안 야근 피로도를 최소화하도록 일할 거다.



# 효율성에서 실패
"""
if n>=sum(works):
    answer=0
else:
    works.sort()
    for _ in range(n):
        works[-1]-=1
        works.sort()
print(sum(i**2 for i in works))
"""




"""
while n>0:
    for j in range(len(works)):
        if n==0:
            break
        elif n>0:
            works[j]-=1
            n-=1
            if n==0: break
    # 남은 일의 양이 없을 때 break
    if sum(works)==0:
        break
    if n==0:
        break
answer=[i**2 for i in works]

print(sum(answer))
"""