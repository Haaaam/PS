for i in range(int(input())):
    n=int(input())
    res=0
    for j in range(1,n+1):
        if j%2!=0:
            res+=j
        else:
            res-=j
    print("#%d %d"%(i+1,res))
