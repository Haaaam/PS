# 피보나치 수는 F(0)=0, F(1)=1일때, 1 이상의 n에 대하여
# F(n)=F(n-1) + F(n-2)가 적용되는 수
def solution(n):
    answer=0
    a,b=0,1
    for i in range(n):
        a,b=a+b,a
    return (a)%1234567
n=3
print(solution(n))
