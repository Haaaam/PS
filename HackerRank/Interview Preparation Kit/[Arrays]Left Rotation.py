n,d=map(int,input().split())
a=list(map(int,input().split()))
def rotLeft(a,d):
    for i in range(d):
        tmp=a[0]
        a.remove(a[0])
        a.append(tmp)
    return a

print(*rotLeft(a,d))
