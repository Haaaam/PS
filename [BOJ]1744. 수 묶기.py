n=sorted([int(input()) for _ in range(int(input()))])

neg,pos,one=[],[],[]
res=0
z=1
for i in n:
    if i <=0:
        neg.append(i)
    elif i>1:
        pos.append(i)
    else:
        one.append(i)

if len(pos)%2==0:
    for i in range(0,len(pos),2):
        res+=(pos[i]*pos[i+1])
else:
    res+=pos[0]
    for i in range(1,len(pos),2):
        res+=(pos[i]*pos[i+1])
if len(neg)%2==0:
    for i in range(0,len(neg),2):
        res+=(neg[i]*neg[i+1])
else:
    res+=neg[-1]
    for i in range(0,len(neg)-1,2):
        res+=(neg[i]*neg[i+1])

if len(one)!=0:
    res+=sum(one)

print(res)



