import heapq

n=int(input())
time=sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x:x[0])
queue=[]
heapq.heappush(queue,time[0][1])

for i in range(1,n):
    if queue[0]>time[i][0]:
        heapq.heappush(queue,time[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue,time[i][1])
print(len(queue))
