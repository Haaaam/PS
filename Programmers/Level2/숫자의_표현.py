def solution(n):
    res = 0
    i = 1
    while n>0:
        if n%i==0:
            res+=1
        n-=i
        i+=1

    return res

n=15

print(solution(n))