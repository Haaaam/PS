a,b=[],[]
res_x,res_y=0,0
for i in range(3):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
for i in range(3):
    if a.count(a[i])==1:
        res_x=a[i]
    if b.count(b[i])==1:
        res_y=b[i]
print(res_x,res_y)