'''import sys
input=sys.stdin.readline
queue=[]
for i in range(int(input())):
    n=int(input())
    queue.append(n)
    queue.sort()
    if len(queue)%2==0:
        if queue[len(queue)//2-1]<queue[len(queue)//2]:
            print(queue[len(queue)//2-1])
        else:
            print(queue[len(queue)//2])

    elif len(queue)%2!=0:
        print(queue[len(queue)//2]) '''
import sys
input=sys.stdin.readline
import heapq
maxq,minq=[],[]
for i in range(int(input())):
    n=int(input())
    if len(maxq)==len(minq):
        heapq.heappush(maxq,(-n,n))
    else:
        heapq.heappush(minq,(n,n))

    if minq and maxq[0][1]>minq[0][1]:
        maxtop=heapq.heappop(maxq)[1]
        mintop=heapq.heappop(minq)[1]
        heapq.heappush(minq,(maxtop,maxtop))
        heapq.heappush(maxq,(-mintop,mintop))
    print(maxq[0][1])
