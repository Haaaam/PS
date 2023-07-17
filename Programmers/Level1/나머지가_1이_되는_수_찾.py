def solution(n):
    answer=0
    res=[]
    for i in range(1,n+1):
        if n%i==1: res.append(i)
        if len(res)!=0: break

    return res[0]
