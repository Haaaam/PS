T=int(input())
a,b,c=0,0,0

while T>=0:
    if T%10!=0:
        break
    if T>=300:
        T-=300
        a+=1
    elif T>=60:
        T-=60
        b+=1
    elif T>=10:
        T-=10
        c+=1
    if T<=0:
        break


if a!=0 or b!=0 or c!=0:
    print(a,b,c)
else:
    print(-1)

