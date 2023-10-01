import math
def solution(n):

    return n//math.gcd(n,6)

# 피자 한판에 6조각
# n의 최대공약수
n=10

print(n//math.gcd(n,6))