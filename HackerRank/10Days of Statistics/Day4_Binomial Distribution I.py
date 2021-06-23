'''
문제: 6명의 아이를 가진 러시아 가정 중에서 3명의 아들을 가질 수 있는 비율은?(소수점 셋째 자리로 나타낼것)
[계산]
1. 남자아이가 태어날 확률 구하기(남자아이/(남자아이+여자아이))
2. 여자아이가 태어날 확률 (1-남자아이가 태어날 확률)

'''
import math
def solution(n,x):
    f=math.factorial
    return f(n)/(f(x)*f(n-x))


a,b=list(map(float,input().split()))

p=a/(a+b)
q=1-p

n=6
pb=0
for i in range(3,n+1):
    pb+=solution(n,i)*(p**i)*(q**(n-i))
    print(i)
print(round(pb,3))

