for i in range(int(input())):
    n=int(input())
    num=list(map(int,input().split()))
    num.sort()
    print("#%d"%(i+1),end=' ')
    print(*num)

    