def solution(l,p,people):
    x=l*p
    res=[]
    for i in people:
        res.append(i-x)
    return res
l,p=map(int,input().split())
people=list(map(int,input().split()))
print(*solution(l,p,people))