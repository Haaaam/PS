import math

"""
짝수일 경우: 값//2=몫 나머지 값%2=0
혹수일 경우: 값//2=몫 나머지 값%2=1

몫과 나머지를 더하면 다음 라운드에 부여받을 번호가 됨. 
"""

def solution(n,a,b):
    answer=0
    if a>b:
        a,b=b,a
    while a!=b:
        a=(a//2)+(a%2)
        b=(b//2)+(b%2)
        answer+=1
        if a==b:
            break

    return answer
"""

def solution(n, a, b):
    answer = 0
    # a를 작은수로 만들기

    if a>b:
        a,b=b,a


    if a+1==b:
        if a==1 and b==2:
            return 1
        elif a-b==-1:
            if a%2!=0:
                return answer
    # 둘이 같을 경우
    if a==b:
        return answer

    for i in range(n // 2):
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        answer += 1

        if ((a + 1) == b) or (a == (b + 1)):
           return answer+1
"""
"""
    for i in range(n // 2):

        if a % 2 == 0:
            a //= 2
        else:
            tmp = a // 2
            a %= 2
            a += tmp
        if b % 2 == 0:
            b //= 2
        else:
            tmp = b // 2
            b %= 2
            b += tmp

        answer += 1
        if (a == 1 and b == 2) or (a == 2 and b == 1):
            return answer + 1
"""
# 대회는 n명이 참가, 토너먼트 형식으로 진행
# a번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번쨰 라운드에서 만나는지 궁금
# n: 게임 참가자 수, a: 참가자 번호, 경쟁자 번호: b
# return 첫 라운드에서 a번을 가진 참가자는 경쟁자로 생각하는 b번 참가자와 몇 번째 라운드에서 만나는지 return
# 단, a번 참가자와 b번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정
n=8
a,b=6,5


print(solution(n,a,b))
"""
for i in range(n//2):
    a=math.ceil(a/2)
    b=math.ceil(b/2)
    answer+=1

    if ((a+1)==b) or(a==(b+1)):
        break

print(answer+1)
"""