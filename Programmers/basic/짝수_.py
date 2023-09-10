def solution(n):
    answer = 0
    for i in range(1, (n // 2) + 1):
        if (i * 2) % 2 == 0:
            answer += (i * 2)
    return answer

n=int(input())
answer=0
for i in range(1,(n//2)+1):
    if (i*2)%2==0:
        answer+=(i*2)
print(answer)