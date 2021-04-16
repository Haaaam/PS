for i in range(int(input())):
    p,q,r,s,w=map(int,input().split())
    a=w*p
    b=0
    if w<=r:
        b=q
    elif w>r:
        b=q+(w-r)*s
    if a>b:
        print("#%d %d"%(i+1,b))
    else:
        print("#%d %d"%(i+1,a))