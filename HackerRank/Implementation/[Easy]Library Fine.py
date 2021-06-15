def libraryFine(d1,m1,y1,d2,m2,y2):
    res=0
    if y1>y2:
        res=10000
    elif y1==y2:
        if m1>m2:
            res=500*(m1-m2)
        elif m1==m2:
            if d1>d2 and (m1-m2)>=0 and (y1-y2)>=0:
                res=15*(d1-d2)
            else:
                res=0
    return res




d1,m1,y1=map(int,input().split())
d2,m2,y2=map(int,input().split())
print(libraryFine(d1,m1,y1,d2,m2,y2))
