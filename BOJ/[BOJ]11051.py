def sol(n,k):
    res=1
    for i in range(n,n-k,-1):res*=i
    for i in range(k,0,-1):res//=i
    return res

n,k=map(int,input().split())
print(sol(n,k)%10007)
