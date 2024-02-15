# 정수 배열 arr과 정수 n
# arr의 길이가 홀수하면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을 return
# arr의 길이가 짝수라면 arr의 모든 홀수 인데스 위치에 n을 더한 배열을 return
def solution(arr,n):
    answer=[]
    # 홀수인 경우
    if len(arr)%2!=0:
        for i in range(len(arr)):
            if i%2==0:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
    else:
        for i in range(len(arr)):
            if i%2!=0:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
    return answer

arr=[49, 12, 100, 276, 33]
n=27
print(solution(arr,n))
