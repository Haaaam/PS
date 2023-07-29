import math
def solution(n):
    if n%math.sqrt(n)==0:
        return (int(math.sqrt(n))+1)**2
    else:
        return -1
n=3
print(solution(n))