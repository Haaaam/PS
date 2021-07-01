def sol(x1,v1,x2,v2):
    if v1>v2:
        if (x2-x1)%(v1-v2)==0:
            return "YES"
    return "NO"
x1,v1,x2,v2=map(int,input().split())
print(sol(x1,v1,x2,v2))
