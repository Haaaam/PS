def Solution(n,volunteer):
    volunteer=sorted(volunteer)
    res=[i for i in range(1,n+1) if i not in volunteer]
    if res:
        return res
    else:
        return "*"

n,r=map(int,input().split())
volunteer=list(map(int,input().split()))
res=[i for i in range(1,n+1) if i not in volunteer]
print(*Solution(n,volunteer))
