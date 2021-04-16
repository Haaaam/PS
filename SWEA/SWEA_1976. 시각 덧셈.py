for i in range(int(input())):
    n=list(map(int,input().split()))
    h=n[0]+n[2]
    m=n[1]+n[3]
    if m>=60:
        h+=1
        m-=60
    if h>12:
        h-=12
    print("#%d %d %d"%(i+1,h,m))

