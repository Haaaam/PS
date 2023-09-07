#저주의 숫자 3
def solution(n):
    answer = 0
    num = list(range(1, 300))
    for i in range(1, n + 1):
        answer += 1
        if answer % 3 == 0 or '3' in str(answer):
            answer += 1
            num[i] = answer
            if answer % 3 == 0 or '3' in str(answer):
                if 30 <= answer < 40 :
                    answer += (40 - num[i])
                    num[i] = answer
                elif 130 <= answer <140:
                    answer+=(140-num[i])
                    num[i]=answer

                else:
                    answer += 1
                    num[i] = answer
        else:
            num[i]=answer

    return num[n]


"""
def solution(n):
    answer=0
    for _ in range(n):
        answer+=1
        while answer % 3==0 or '3' in str(answer):
            answer+=1
    return answer
"""
n=40


print(solution(n))



