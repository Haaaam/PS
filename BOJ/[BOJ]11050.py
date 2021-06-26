'''n,k=map(int,input().split())
def sol(num):
    if num==0 or num==1:
        return 1
    return sol(num-1)*num
print(int(sol(n)/(sol(n-k)*sol(k))))'''
import math
n,k=map(int,input().split())
def sol(n,k):
    if n==0 or n==k:
        return 1
    return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))
print(int(sol(n,k)))