from collections import deque
for i in range(int(input())):
    n,m=map(int,input().split())
    queue=deque(map(int,input().split()))
    cnt=0#순서
    while queue:
        top=max(queue)
        m-=1
        pop=queue.popleft()
        #타겟이 아닐 경우
        if top!=pop:
            queue.append(pop)
            if m<0:
                m=len(queue)-1
        #맞을경우
        else:
            cnt+=1
            if m==-1:
                print(cnt)
                break