# n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 한다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면
# -1을 리턴하는 함수를 완성하시오.
"""
import math
def solution(n):
    if n%math.sqrt(n)==0:
        return int(math.sqrt(n)+1)**2
    else:
        return -1
"""
def solution(n):
    sqrt=n**(1/2) # 제곱근
    if n%sqrt==0:
        return int(sqrt+1)**2
    else:
        return -1
n=121
print(solution(n))
