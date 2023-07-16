def solution(number):

    s=0
    for i in number: s+=int(i)
    answer= s%9

    return answer

number="123"
print(solution(number))

