from collections import deque
n,m=map(int,input().split())
array=list(map(int,input().split()))
cnt=0#회전 횟수
queue=deque([i for i in range(1,n+1)])
while array:
    #queue의 첫번째 원소가 뽑으려는 수와 같을 경우
    if array[0]==queue[0]:
        queue.popleft()
        array.pop(0)
    else:
        #뽑으려는 수의 위치가 queue의 길이 절반보다 작거나 같을 경우
        if queue.index(array[0])<=len(queue)//2:
            #왼쪽으로 한칸 이동
            while queue[0]!=array[0]:
                cnt+=1
                temp=queue.popleft()
                queue.append(temp)

        else:
            #뽑으려는 수의 위치가 queue의 길이 절반보다 큰경우
            #오른쪽으로 한 칸 이동
            while queue[0]!=array[0]:
                cnt+=1
                temp=queue.pop()
                queue.insert(0,temp)

print(cnt)



