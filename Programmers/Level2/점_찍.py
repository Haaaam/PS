# x축과 y축이 직교하는 2차원 좌표평면에 점을 찍으면서 놀고 있습니다.
# 진수는 두 양의 정수 k, d가 주어질 때 다음과 같이 점을 찍으려 합니다.
# 원점(0,0)으로부터 x축 방향으로 a*k(a=0,1,2,3,,,,), y축 방향으로 b*k(b=0,1,2,3,,,,)만큼 떨어진 위치에 점을 찍습니다.
# 원점과 거리가 d를 넘는 위치에는 점을 찍지 않습니다.
"""
# 시간초과
import math
def solution(k, d):
    answer = 0
    for i in range(0,d+1,k):
        for j in range(0,d+1,k):
            if math.sqrt(i**2+j**2)<=d:
                print(i,j)
                answer+=1
    return answer
"""
# 피타고라스의 정리로 접근하기

# d**2=x**2+y**2
# x**2=d**2-y**2
# y축을 포함한 총 점의 갯수=x의 길이를 k개로 나눈 몫+1
# ==> for문을 한개만 써서 거리 d를 초과하지 않는 (x,y) 전체 점의 갯수를 구할 수 있음
import math

def solution(k,d):
    answer=0
    for y in range(0,d+1,k):
        x=d**2-y**2
        cnt=math.sqrt(x)//k+1
        answer+=cnt
    return int(answer)
k,d=1,5
print(solution(k,d))