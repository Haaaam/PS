import math
def solution(n):
    x=math.sqrt(n)
    if x%1==0:
        answer=(x+1)**2
    else:
        answer=-1
    return answer
n=int(input())
print(solution(n))
