import math
def solution(nums):
    hash = {}

    for i in nums:
        if str(i) not in hash:
            hash[str(i)] = 1
        else:
            hash[str(i)] += 1

    if len(nums) // 2 > len(hash):
        answer = len(hash)

    else:
        answer = len(nums)//2
    return answer

nums=[3,3,3,2,2,4]
print(solution(nums))
