from math import factorial as f
def solution(n,x):
    return f(n)/(f(x)*f(n-x))

def b(x,n,p):
    return solution(n,x)*p**x*(1-p)**(n-x)

p,n=list(map(int,input().split()))

res1=sum([b(i,n,p/100) for i in range(3)])
res2=sum([b(i,n,p/100) for i in range(2,n+1)])
print(round(res1,3))
print(round(res2,3))


