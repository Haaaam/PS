n=int(input())
p=int(input())

def pageCount(n,p):
    n=n//2
    p=p//2
    return min(p,n-p)
print(pageCount(n,p))