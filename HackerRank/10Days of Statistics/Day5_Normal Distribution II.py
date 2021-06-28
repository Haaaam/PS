import math
def sol(x,m,sd):
    return  0.5*(1+math.erf((x-m)/(sd*math.sqrt(2))))
m,sd=map(int,input().split())
u,l=int(input()),int(input())

#80
print(round((1-sol(u,m,sd))*100,2))
print(round((1-sol(l,m,sd))*100,2))
print(round(sol(l,m,sd)*100,2))