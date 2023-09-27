def solution(n):
    answer=[]
    for i in range(1, n + 1):
        if n % i == 0:
            answer.append(i)
    return answer

n=25
answer=[]
"""
for i in range(1,n+1):
    if n%i==0:
        answer.append(i)
"""
for i in range(1,int(n**(1/2))+1):
    if n%i==0:
        answer.append(i)
        if n//i not in answer:
            answer.append(n//i)

print(sorted(answer))
