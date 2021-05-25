#최소공약수 or 브레젠험 알고리즘 활용
import math

w,h=map(int,input().split())
def solution(w,h):
    return w*h-(w+h-math.gcd(w,h))
print(solution(w,h))

