def sol(num,p):
    return (1-p)**(num-1)*p

n,p=list(map(int,input().split()))
num=int(input())
print(round(sol(num,n/p),3))
