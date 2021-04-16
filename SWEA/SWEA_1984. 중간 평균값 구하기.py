for i in range(int(input())):
    test=list(map(int,input().split()))
    first=min(test)
    last=max(test)
    res=sum(test)-first-last
    print("#%d %d"%(i+1,round(res/8)))

