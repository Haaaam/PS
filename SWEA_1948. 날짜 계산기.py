date=[31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(int(input())):
    m=list(map(int,input().split()))
    m1,m2=m[0],m[2]
    d1,d2=m[1],m[3]
    res=0
    if m1==m2:
        res+=d2-d1+1
    else:
        res+=(date[m1-1]-d1+1)+sum(date[m1:m2-1])+d2
    print("#%d %d"%(i+1,res))
