from math import gcd # 최대 공약수 구하는 라이브러리
def solution(numer1, denom1, numer2, denom2):
    up = numer1 * denom2 + numer2 * denom1
    down = denom1 * denom2

    a = gcd(up, down)
    answer = [up // a, down // a]

    return answer

numer1,denom1=1,2
numer2,denom2=3,4


up=numer1*denom2+numer2*denom1
down=denom1*denom2

a=gcd(up,down)
answer=[up//a,down//a]

print(answer)