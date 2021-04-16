for i in range(int(input())):
    #n:상자의 갯수 , q: 작업 수행의 갯수
    n,q=map(int,input().split())
    res=[0]*n
    for j in range(1,q+1):
        l,r=map(int,input().split())
        for k in range(l-1,r):
            res[k]=j
    print(f'#{i+1}',*res)

