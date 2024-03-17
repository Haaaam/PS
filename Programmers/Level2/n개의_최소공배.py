# 두 수의 최소공배수란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미
# n개의 최소공배수는 n개의 수들의 배수 중 공통이 되는 가장 작은 숫자
# return n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수
import math
def solution(arr):
    answer = 0

    while len(arr)>=2:
        # 최소공배수: 두 수의 배수중 공통이 되는 가장 작은 숫자를 의미
        # 그러므로 a,b 두개의 숫자를 arr로 부터 pop()
        # arr에 a와b의 최소공배수 담기
        a=arr.pop()
        b=arr.pop()
        arr.append((a*b)//math.gcd(a,b))

    return arr[-1]

arr=[2,6,8,14]
print(solution(arr))