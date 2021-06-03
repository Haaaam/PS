def beautifulDays(i,j,k):
    cnt=0
    for x in range(i,j+1):
        a,b='',''
        for y in str(x):
            a+=y
        b=int(str(a)[::-1])
        if abs(int(a)-b)%k==0:
            cnt+=1
    return cnt

i,j,k=map(int,input().split())
print(beautifulDays(i,j,k))
