def solution(n):
    array=[True]*(n+1)
    result=[]
    for i in range(2,n+1):
        if array[i]:
            result.append(i)
        for j in range(2*i,n+1,i):
            array[j]=False
    return len(result)
n=int(input())
print(solution(n))