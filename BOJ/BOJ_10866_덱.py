from collections import deque
import sys
input=sys.stdin.readline
queue=deque()
for i in range(int(input())):
    a=input().split()
    #push_back X:정수 X를 덱의 뒤에 넣는다.
    if a[0]=="push_back":
        queue.append(a[1])
    #push_front X:정수 X를 덱의 앞에 넣는다.
    elif a[0]=="push_front":
        queue.insert(0,a[1])
    #pop_front:덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다.
    # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력
    elif a[0]=="pop_front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    #pop_back X:덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력
    #만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력
    elif a[0]=="pop_back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
            queue.pop()
    #size:덱에 들어있는 정수의 개수를 출력
    elif a[0]=="size":
        print(len(queue))
    #empty:덱이 비어있으면 1을, 아니면 0을 출력
    elif a[0]=="empty":
        if not queue:
            print(1)
        else:
            print(0)
    #front:덱의 가장 앞에 있는 수를 출력
    #만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력
    elif a[0]=="front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    #back:덱의 가장 뒤에 있는 정수를 출력
    #만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력
    elif a[0]=="back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])

