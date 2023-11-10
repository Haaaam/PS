def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i, number in enumerate(numbers):
        #  numbers의 idx를 stack에 넣기
        # number[stack[-1]]의 크기가 현재 number보다 작을 경우 stack[-1]의 위치의 값을 number로 대체
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(i)
    return answer

# 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return하도록 solution 함수를 완성 하시요.
# 단, 뒷 큰수가 존재하지 않는 원소는 -1을 담는다.
numbers=[2,3,3,5]
answer=[-1]*len(numbers)
stack=[]
for i,number in enumerate(numbers):
    while stack and numbers[stack[-1]]<number:
        answer[stack.pop()]=number
    stack.append(i)

print(answer)


