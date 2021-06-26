n,k=map(int,input().split())
def sol(num):
    if num==0 or num==1:
        return 1
    return sol(num-1)*num
print(int(sol(n)/(sol(n-k)*sol(k))))