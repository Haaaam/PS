def solution(numbers,direction):
    answer = []
    if direction == 'right':
        answer.append(numbers[-1])
        for i in numbers[:-1]:
            answer.append(i)

    else:
        answer = numbers[1:]
        answer.append(numbers[0])

    return answer

numbers=[1,2,3]
direction='right'
answer=[]
if direction=='right':
    answer.append(numbers[-1])
    for i in numbers[:-1]:
        answer.append(i)

else:
    answer=numbers[1:]
    answer.append(numbers[0])

print(answer)