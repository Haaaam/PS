for i in range(int(input())):
    l=list(map(int,input().split()))
    res = 0
    for j in l:
        res+=j
    print("#%d %d"%(i+1,round(res/10)))