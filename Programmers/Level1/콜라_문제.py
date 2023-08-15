def solution(a,b,n):
    cola=0
    while not a > n:
        i = 0
        i += (n // a)
        n = n - (i * a) + (i * b)

        cola += i*b
    return cola

# 콜라 빈 병 2개를 가져다주면 콜라 1병을 주는 마트
# 빈병 20개를 가져다 주면?, 빈병이 2개 미만이면 콜라 못 받음

a,b,n=2,1,20
cola=0


while not a>n:

    i=0
    i+=(n//a)
    n=n-(i*a)+(i*b)

    cola+=i*b


print(cola)