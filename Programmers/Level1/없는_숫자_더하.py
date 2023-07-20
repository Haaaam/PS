def solution(numbers):
    answer = 0
    numbers=sorted(numbers)
    for i in range(10):
        if i not in numbers:
            answer+=i

    return answer

numbers=[5,8,4,0,6,7,9]
numbers=sorted(numbers)
print(numbers)
print(solution(numbers))