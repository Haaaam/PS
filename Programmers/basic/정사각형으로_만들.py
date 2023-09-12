def solution(arr):
    answer = arr

    # 행이 열보다 큰 경우
    if len(arr) > len(arr[0]):
        for i in range(len(arr)):
            for j in range(len(arr) - len(arr[i])):
                answer[i].append(0)
    # 행이 열보다 작은 경우
    else:
        for i in range(len(arr[0]) - len(arr)):
            answer.append([0] * len(arr[0]))
    return answer

arr=[[1, 1], [1, 1], [1, 1], [1, 1]]




print(solution(arr))