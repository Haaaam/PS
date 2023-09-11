def solution(str_list):
    answer=[]
    idx=0
    for i in str_list:
        if i=='l':
            answer=str_list[:idx]
            break
        elif i=="r":
            answer=str_list[idx+1:]
            break
        idx+=1

    return answer

str_list=["l"]

print(solution(str_list))
