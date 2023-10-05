def solution(angle):

    if angle > 0 and angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle > 90 and angle < 180:
        answer = 3
    else:
        answer = 4
    return answer

angle=70
answer=0
if angle >0 and angle<90:
    answer=1
elif angle==90:
    answer=2
elif angle>90 and angle <180:
    answer=3
else:
    answer=180
print(answer)