def sol(n,wine):
    d=[0]*10000
    for i in range(n):
        if i==0:
            d[0]=wine[0]
            continue
        elif i==1:
            d[1]=wine[0]+wine[1]
            continue
        elif i==2:
            d[2]=max(wine[i]+d[i-2],wine[i]+wine[i-1],d[i-1])
            continue
        d[i] = max(wine[i] + wine[i - 1] + d[i - 3], wine[i] + d[i - 2], d[i - 1])
    return max(d)


n=int(input())
wine=[int(input()) for _ in range(n)]

print(sol(n,wine))


