n=int(input())
def solution(n):
    answer = 0
    three=[]
    while n>0:
        three.append(n%3)
        if n//3==1:
            three.append(1)
            break
        n=n//3
    three.reverse()
    for i in range(len(three)):
        answer+=three[i]*(3)**i
    return answer
print(solution(n))