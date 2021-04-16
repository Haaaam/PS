for i in range(int(input())):
    n=int(input())
    speed=0
    move=0
    for j in range(n):
        c=list(map(int,input().split()))
        if c[0]==1:
            speed+=c[1]
        elif c[0]==2:
            if c[0]>speed:
                speed=0
            else:
                speed-=c[1]
        move+=speed
    print("#%d %d"%(i+1,move))

    