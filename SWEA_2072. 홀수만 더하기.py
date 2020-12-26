for i in range(int(input())):
    num=list(map(int,input().split()))
    res=0
    for j in num:
        if j%2!=0:
            res+=j
    print("#%d %d"%(i+1,res))
    