def solution(n):
    array=[True]*(n+1)
    res=[]
    for i in range(2,n+1):
        if array[i]:
            res.append(i)
        for j in range(2*i,n+1,i):
            array[j]=False

    return len(res)

n=10

print(solution(n))
