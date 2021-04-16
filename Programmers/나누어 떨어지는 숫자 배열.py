def solution(arr,divisor):
    answer=[]
    arr.sort()
    for i in arr:
        if i%divisor==0:
            answer.append(i)
    if len(answer)==0:
        answer.append(-1)
    return answer
arr=list(map(int,input().split()))
divisor=int(input())
print(solution(arr,divisor))
