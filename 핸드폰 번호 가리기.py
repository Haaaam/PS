def solution(phone_number):
    answer=phone_number[-4:]
    return "*"*(len(phone_number)-4)+answer
answer=input()
print(solution(answer))
