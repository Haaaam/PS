# 치킨 쿠폰
def solution(chicken):
    answer = 0

    while chicken >= 10 :
        eaten=chicken//10 # 먹고 받을 수 있는 쿠폰
        answer+=eaten # 먹은것
        chicken=chicken%10+eaten

    return answer

chicken=1081

print(solution(chicken))


