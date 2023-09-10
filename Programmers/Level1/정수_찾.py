def solution(num_list, n):

    if n in num_list:
        return 1
    else:
        return 0

num_list=[1,2,3,4,5]
n=3
print(solution(num_list,n))
