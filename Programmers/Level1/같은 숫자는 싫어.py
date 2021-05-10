def solution(arr):
    answer = []
    front=arr[0]
    answer.append(front)
    for i in range(1,len(arr)):
        if front!=arr[i]:
            answer.append(arr[i])
            front=arr[i]
    return answer
arr=list(map(int,input().split()))
print(solution(arr))