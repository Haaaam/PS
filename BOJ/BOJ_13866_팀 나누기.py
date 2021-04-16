n=list(map(int,input().split()))
a=min(n)
b=max(n)
n.remove(a)
n.remove(b)
c=sum(n)
if a+b>c:
    print((a+b)-c)
else:
    print(c-(a+b))