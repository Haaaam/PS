s=input()
def solution(s):
    answer = ''
    tmp = [int(i) for i in s.split()]
    answer += str(min(tmp))
    answer += ' '
    answer += str(max(tmp))

    return answer
print(solution(s))

