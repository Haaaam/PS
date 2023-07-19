def solution(a, b):
    res = 0
    if a>b:
        for i in range(b,a+1):
            res+=i
    elif a==b:
        res=a
    else:
        for i in range(a,b+1):
            res+=i
    return res

def adder(a,b):
    if a>b:
        a,b=b,a

    return sum(range(a,b+1))
a,b=3,5
print(adder(a,b))


a,b=3,3
res=0
if a>b:
    for i in range(b,a+1):
        res+=i
elif a==b:
    res=a
else:
    for i in range(a,b+1):
        res+=i
print(res)