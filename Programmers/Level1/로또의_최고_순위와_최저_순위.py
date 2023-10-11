def solution(lottos, win_nums):

    cnt = 0
    # 0이 없는 경우
    zero=lottos.count(0) if 0 in lottos else 0 # 0의 갯수
    for i in win_nums:
        if i in lottos:
            cnt += 1

    if cnt > 0:
        return [6 - (zero + cnt) + 1, 6 - cnt + 1]
    # 맞는 숫자가 없는 경우
    else:
        # 0이 있는 경우
        if zero!=0:
            return [6 - (zero + cnt) + 1, 6]
        # lottos에 0이 없는 경우 예외 처리
        else:
            return [6-(zero+cnt),6]

# 순위 1: 6개 번호 모두 일치
# 순위 2: 5개 번호 일치 ~ 순위 5: 2개 번호 일치
# 순위 6(낙첨)

# 민우 동생이 로또에 낙서를 함. 일부 번호를 볼 수 없음.
# 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어짐
# 알 수 없는 번호를 0으로 표기
lottos=[1,2,3,4,5,6] # 로또
win_nums=[7,8,9,10,11,12] # 우승 번호

cnt=0

zero=lottos.count(0) if 0 in lottos else 0 # 0의 갯수

for i in win_nums:
    if i in lottos:
        cnt+=1

if cnt>0:
    print([6 - (zero + cnt)+1, 6 - cnt + 1])
else:
    if zero!=0:
        print([6 - (zero + cnt)+1, 6])
    else:
        print([6 - (zero+cnt), 6])
