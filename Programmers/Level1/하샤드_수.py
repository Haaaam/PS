def solution(x):
    answer = True
    res=0
    for i in list(str(x)):
        res+=int(i)
    if x%res!=0:
        answer=False
    return answer

x=11

print(solution(x))
