def solution(num_list):

    if num_list[-1] >num_list[-2]:
        num_list.append(num_list[-1]-num_list[-2])
    else:
        num_list.append(2*num_list[-1])
    return num_list
num_list=[2,1,6]
print(solution(num_list))
