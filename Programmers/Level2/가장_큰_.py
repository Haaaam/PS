def solution(numbers):
    numbers = list(map(str, numbers))
    # numbers의 원소는 0 이상 1,000 이하입니다.
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)

    if numbers[0]=='0':
        return '0'
    return ''.join(numbers)

numbers=[3, 30, 34, 5, 9]
# 0또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수

print(solution(numbers))






