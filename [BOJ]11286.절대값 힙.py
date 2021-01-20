import heapq
import sys
input=sys.stdin.readline
n=int(input())
array=[]
for i in range(n):
    num=int(input())
    if num!=0:
        heapq.heappush(array,(abs(num),num))
        print(array)
    else:
        if not array:
            print(0)
        else:
            print(heapq.heappop(array)[1])


