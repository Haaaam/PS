def solution(x,n):
    answer=[]
    for i in range(1,n+1):
        answer.append(i*x)
    return answer
n=int(input())
x=int(input())
print(solution(x,n))