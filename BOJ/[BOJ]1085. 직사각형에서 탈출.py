x,y,w,h=map(int,input().split())
def sol():
    res=min(w-x,x)
    res=min(res,min(h-y,y))
    return res

print(sol())

