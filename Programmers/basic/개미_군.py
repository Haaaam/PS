# 장군개미 5의 공격력, 병정개미 3의 공격력, 일개미 1의 공격력

"""
#처음 짠 코드
def solution(hp):
    answer=0
    if hp//5>0:
        answer+=hp//5
        hp-=(hp//5)*5
    if hp//3>0:
        answer+=hp//3
        hp-=(hp//3)*3
    if hp>0:
        answer+=hp

    return answer

"""
# code refactoring
def solution(hp):


    return (hp//5)+((hp%5)//3)+((hp%5)%3)

hp=23
print(solution(hp))