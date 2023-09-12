def solution(n):
    pizza=0
    pizza+=n//7

    if n%7!=0:
        pizza+=1

    return pizza
n=int(input())
print(solution(n))
