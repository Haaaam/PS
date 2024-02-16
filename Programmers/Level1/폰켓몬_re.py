# 총 n 마리의 폰켓몬 중에서 n/2마리를 가져가도 좋다고 함
# 연구실의 폰켓몬은 종류에 따라 번호를 붙여 구분(같은 종류의 폰켓몬은 같은 번호를 가진다)
# 최대한 다양한 종류의 폰켓몬을 가져가길 원한다.
# n마리 폰켓몬의 종류 번호가 담긴 배열 nums
# n/2 마리의 폰켓몬을 선택하는 방법 중
# 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아 그때의 폰켓몬 종류 번호의 개수를 return

def solution(nums):

    # 폰켓몬의 종류 번호마다 몇마리가 있는지 dictionary에 담기
    phonketmon={}
    for i in nums:
        if i not in phonketmon.keys():
            phonketmon[i]=1
        else:
            phonketmon[i]+=1
    # 전체 폰켓몬의 n//2가 폰켓몬의 종류보다 많은 경우
    if len(nums)//2>len(phonketmon):
        answer=len(phonketmon)
    # 전체 폰켓몬의 n/2가 폰켓몬의 종류보다 적은 경우
    else:
        answer=len(nums)//2

    return answer

nums=[3,1,2,3]
print(solution(nums))
