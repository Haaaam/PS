#2021.02.17
#[BOJ]11279. 최대 힙
import heapq
import sys
input=sys.stdin.readline
h=[]
for i in range(int(input())):
    x=int(input())
    heapq.heappush(h,-x)
    if x==0:
        print(-h[0])
        heapq.heappop(h)
