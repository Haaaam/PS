# n개의 음이 아닌 정수들이 있다.
# 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 한다.
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서
# 타겟 넘버를 만드는 방법의 수를 return
def solution(numbers, target):
    answer = 0
    visited=[0]
    for i in range(len(numbers)):
        tmp=[]
        for v in visited:
            tmp.append(v+numbers[i])
            tmp.append(v-numbers[i])
        visited=tmp
    for v in visited:
        if v==target:
            answer+=1
    return answer

numbers=[4, 1, 2, 1]
target=4
print(solution(numbers,target))
