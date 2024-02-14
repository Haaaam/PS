# 붕대 감기
# t초동안 붕대를 감으면서 1초마다 x만큼의 체력을 회복한다.
# t초 연속으로 붕대를 감는 데 성공한다면 y만큼의 체력을 추가로 회복
# bandage: 시전 시간, 초당 회복량, 추가 회복량
# attacks: 공격 시간, 피해량
# 만약 몬스터의 공격을 받고 캐릭터의 체력이 0 이하가 되어 죽는다면 -1을 return
def solution(bandage, health, attacks):
    answer = health
    f_t, f_b = attacks[0][0], attacks[0][1]
    answer -= f_b

    for i in range(1, len(attacks)):
        a_t, a_b = attacks[i][0], attacks[i][1]

        elapsed_time = a_t - f_t - 1
        # 시전시간과 같거나 큰경우
        if elapsed_time >= bandage[0]:
            answer += (bandage[1] * elapsed_time)
            answer += bandage[2] * (elapsed_time // bandage[0]) # 추가 회복량

        # 시전시간보다 작은 경우
        else:
            answer += (bandage[1] * elapsed_time)

        answer = min(health, answer)  # 최대 체력 초과 방지
        answer -= a_b

        if answer <= 0:
            return -1
        f_t = a_t

    return answer

bandage=[3,10,1]
health=100
attacks=[[1,5],[3,5]]
print(solution(bandage,health,attacks))