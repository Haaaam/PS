for i in range(int(input())):
    n=int(input())
    money=[50000,10000,5000,1000,500,100,50,10]
    cnt=[0]*len(money)
    print("#%d"%(i+1))
    for j in range(len(money)):
        cnt[j]+=n//money[j]
        n%=money[j]
    for c in cnt:
        print(c,end=' ')
    print()