def solution(s):
    answer = ''
    tmp=[int(i) for i in s.split()]
    answer+=str(min(tmp))
    answer+=' '
    answer+=str(max(tmp))
    return answer

s="-1 -2 -3 -4"
print(solution(s))