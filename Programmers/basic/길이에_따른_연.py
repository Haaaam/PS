# 리스트의 길이가 11이상이면 리스트에 있는 모든 원소의 합을 return
# 10이하이면 모든 원소의 곱을 return
def solution(num_list):

    if len(num_list)>=11:
        return sum(num_list)
    else:
        answer=1
        for i in num_list:
            answer*=i
        return answer

num_list=[3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
print(solution(num_list))