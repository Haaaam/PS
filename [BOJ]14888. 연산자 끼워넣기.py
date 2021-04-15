n=int(input())
a=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
# 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다.
min_,max_=1e9,-1e9

def op(i,res,add,sub,mul,div):
    global min_,max_
    if i==n:
        max_=max(res,max_)
        min_=min(res,min_)
        return
    else:
        if add:
            op(i+1,res+a[i],add-1,sub,mul,div)
        if sub:
            op(i+1,res-a[i],add,sub-1,mul,div)
        if mul:
            op(i+1,res*a[i],add,sub,mul-1,div)
        if div:
            op(i+1,int(res/a[i]),add,sub,mul,div-1)
op(1,a[0],add,sub,mul,div)
print(max_)
print(min_)

