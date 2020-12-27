for i in range(int(input())):
    n=int(input())
    arr=[0]*10
    k=1
    cnt=0
    while cnt!=10:
        num=str(n*k)
        for j in num:
            if arr[int(j)]==0:
                arr[int(j)]=1
                cnt+=1
        k+=1

    print("#%d %d"%(i+1,n*(k-1)))

