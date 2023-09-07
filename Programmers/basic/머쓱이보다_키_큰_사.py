def solution(array, height):
    answer=0
    for i in array:
        if height < i:
            answer += 1
    return answer

array=[149,180,192,170]
height=167
answer=0
for i in array:
    if height <i:
        answer+=1
print(answer)