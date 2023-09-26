# 구하고자 하는 수의 제곱근만큼 for문 돌려서 약수 구하기
# 이중 for문으로 구하면 시간 초과 남...
def solution(number, limit, power):

    nums=[]

    answer = 0

    # 약수 갯수 구하기
    for i in range(1, number + 1):
        cnt = 0
        # 1부터 i의 제곱근 까지 for문 돌리기
        for j in range(1, int(i ** (1 / 2)) + 1):
            if i % j == 0:
                cnt += 1
                # 제곱이 되는 수는 count 1을 하여 중복 방지
                if j ** 2 != i:
                    cnt += 1
        nums.append(cnt)

    # print(nums.count())
    for i in range(len(nums)):
        # 공격력이 제한 수치를 넘는 경우
        if nums[i] > limit:
            answer += power
        else:
            answer += nums[i]

    return answer
# 공격력의 제한수치를 정하고, 제한수치보다 큰 공격력을 가진 무기를 구매해야 하는 기사는 협약기관에서 정한 공격력을 가진 무기 구매

# number: 기사단원의 수, limit: 공격력의 제한수치, power: 사용할 무기의 공격력


number,limit,power=10,3,2
nums = []

answer = 0

# 약수 갯수 구하기
for i in range(1, number + 1):
    cnt = 0
    # 1부터 i의 제곱근 까지 for문 돌리기
    for j in range(1, int(i ** (1 / 2)) + 1):
        if i % j == 0:
            cnt += 1
            # 제곱이 되는 수는 count 1을 하여 중복 방지
            if j ** 2 != i:
                cnt += 1
    nums.append(cnt)

# print(nums.count())
for i in range(len(nums)):
    # 공격력이 제한 수치를 넘는 경우
    if nums[i] > limit:
        answer += power
    else:
        answer += nums[i]
print(answer)