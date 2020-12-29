for k in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    res=0
    for _ in range(n):
        l.append(list(map(int,input().split())))
    for i in range(n-m+1):
        for j in range(n-m+1):
            t=0
            for x in range(i,i+m):
                for y in range(j,j+m):
                    t+=l[x][y]
            if t>res:
                res=t
    print('#{} {}'.format(k+1,res))

    