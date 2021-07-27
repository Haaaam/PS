'''
n:Bobby's initial amount of money
c:the cost of a chocolate bar
m:the number of wrappers he can turn in for a free bar
'''

def sol(n,c,m):
    eat=0
    w=0
    ch=n//c
    while ch>0:
        eat+=ch
        w+=ch
        ch=0
        if w!=0:
            ch+=w//m
            w=w%m
    return eat
t=int(input())
for i in range(t):
    n,c,m=map(int,input().split())
    print(sol(n,c,m))