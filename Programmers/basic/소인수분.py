# 소인수분해란 어떤 수를 소인들의 곱으로 표현하는 것
# 12를 소인수 분해하면 2*2*3으로 나타낼 수 있다.
# 12의 소인수는 2와 3이다.
# n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution함수 완성하기
import math
def solution(n):
    answer = []
    d=2 # 소인수분해는 2부터 시작하므로 d는 2로 초기화

    while d<=n:
        if n%d==0:
            if d not in answer:
                answer.append(d)
            n//=d
        else:
            d+=1 # d로 나누어 지지 않을 경우 d+1
    return answer
n=12
print(solution(n))