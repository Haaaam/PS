def solution(num_list,n):
    answer=num_list[n:]+num_list[:n]
    return answer
num_list=[5,2,1,7,5]
n=3

print(solution(num_list,n))