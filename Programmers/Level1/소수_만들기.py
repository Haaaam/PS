from itertools import combinations
def sosu(num):
    if num==0 or num==1:
        return False
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True


def solution(nums):
    answer = 0
    for i in combinations(nums,3):
        if sosu(sum(i)):
            answer+=1

    return answer

nums=[1,2,7,6,4]

print(solution(nums))
