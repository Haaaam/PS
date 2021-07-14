def sol(n,p):
    x_p_index=[p.index(i)+1 for i in range(1,n+1)]
    res=[p.index(i)+1 for i in x_p_index]
    return res

n=int(input())
p=list(map(int,input().split()))
for i in sol(n,p):
    print(i)

