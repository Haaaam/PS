# 주어진 숫자 중 3개의 수를 더했을 때 소수가 된는 경우의 개수를 구하려고 한다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는
# 경우의 개수를 return 하도록 solution 함수 완성하기
"""
def solution(nums):
    answer = 0


    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                sum_num=nums[i]+nums[j]+nums[k]

                # 소수 확인
                for t in range(2,round(sum_num/2)):
                    if sum_num%t==0:
                        break
                else:
                    answer+=1

    return answer
"""

from itertools import combinations

def solution(nums):
    answer = 0

    for i in combinations(nums,3):
        sum_num=sum(i)
        check=True

        # 소수 확인
        for j in range(2,int(sum_num**(1/2))+1):
            # 소수가 아닌 경우
            if sum_num%j==0:
                check=False
                break
        # 소수인 경우
        if check:
            answer+=1

    return answer

nums=[1,2,3,4]
print(solution(nums))