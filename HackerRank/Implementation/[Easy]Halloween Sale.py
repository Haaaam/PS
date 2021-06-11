def howManyGame(p,d,m,s):
    cnt=1
    sum=p
    while p>=m:
        if sum>s:
            return cnt-1

        else:
            cnt+=1
            p-=d
            if p<m:
                p=m
            sum += p




p,d,m,s=map(int,input().split())
print(howManyGame(p,d,m,s))