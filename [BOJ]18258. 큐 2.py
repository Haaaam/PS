from collections import deque
import sys
queue=deque()
input=sys.stdin.readline

for i in range(int(input())):
    a=input().split()
    if a[0]=="push":
        queue.append(a[1])
    elif a[0]=="pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif a[0]=="size":
        print(len(queue))
    elif a[0]=="empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif a[0]=="front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif a[0]=="back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])

