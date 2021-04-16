n,s=map(int,input().split())
bro=list(map(int,input().split()))
def gcd(a,b):
    tmp=a%b
    while tmp:
        a=b
        b=tmp
        tmp=a%b
    return b

for i in range(n):
    bro[i]=abs(s-bro[i])

result = bro[0]
for i in range(1,n):
    if bro[i]>=result:
        result=gcd(bro[i],result)
    else:
        result=gcd(result,bro[i])
print(result)


