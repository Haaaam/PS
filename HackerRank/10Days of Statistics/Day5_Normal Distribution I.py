import math

def sol(x,m,sd):
    return 0.5*(1+math.erf((x-m)/(sd*math.sqrt(2))))


m,sd=map(int,input().split())
x=float(input())
low,up=map(int,input().split())
print(round(sol(x,m,sd),3))
print(round(sol(up,m,sd)-sol(low,m,sd),3))