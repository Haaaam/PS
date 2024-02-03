# arr의 앞에서부터 차례대로 원소를 보면서 원소가 a라면 X의 맨 뒤에 a를 a번 추가하는 일을 반복한 뒤의 배열 X를 return
def solution(arr):
    answer=[]
    for i in arr:
        for j in range(i):
            answer.append(i)

    return answer

arr=[5,1,4]
print(solution(arr))