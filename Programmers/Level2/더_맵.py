import heapq
def solution(scoville,K):

    cnt = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    #heap[0]은 heap의 최솟값을 나타냄
    while heap[0] < K:
        taste = heapq.heappop(heap) + (heapq.heappop(heap) * 2)
        heapq.heappush(heap, taste)
        cnt += 1
        if len(heap) == 1 and heap[0] < K:
            return -1

    return cnt

# 섞은 음식의 스코빌 지수=가장 맵지 않은 음식의 스코빌 지수+(두번째로 맵지않은 음식의 스코빌 지수*2)
# 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞기
scoville=[2,1,3,9,10,12]
K=7
taste=0
cnt=0
heap=[]
for i in scoville:
    heapq.heappush(heap,i)

while heap[0]<K:
    taste=heapq.heappop(heap)+(heapq.heappop(heap)*2)
    heapq.heappush(heap,taste)
    cnt+=1
    if scoville[0]<K and len(heap)==1:
        cnt=-1
        break

    print(heap)
print(cnt)