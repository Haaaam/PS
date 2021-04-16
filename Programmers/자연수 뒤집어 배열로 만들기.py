def solution(n):
    answer=[]
    for i in str(n):
        answer.append(i)
    answer.reverse()
    return list(map(int,answer))
n=int(input())
print(solution(n))

