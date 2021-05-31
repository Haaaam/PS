def angryProfessor(k,a):
    cnt=0
    global n
    for i in a:
        if i<=0:
            cnt+=1
    if cnt>=k:
        return 'NO'
    else:
        return 'YES'

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    print(angryProfessor(k,a))