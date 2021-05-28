#def minimumBribes(q):

for i in range(int(input())):
    n=int(input())
    tmp=[k for k in range(1,n+1)]
    q=list(map(int,input().split()))
    cnt=0
    for j in range(n):
        if q[j]-tmp[j]>2:
            print('Too chaotic')
            cnt=0
            break
        elif q[j]-tmp[j]>0:
            cnt+=q[j]-tmp[j]
    if cnt!=0:
        print(cnt)
