# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴
def solution(n):
    answer=0
    for i in range(1,n+1):
        if n%i==0:
            answer+=i

    return answer

n=12
print(solution(n))