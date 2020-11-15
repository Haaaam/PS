def solution(n, m):

    for i in range(1,m+1):
        if n%i==0 and m%i==0:
            answer = []
            answer.append(i)
            res=(n//i)*(m//i)*i
            answer.append(res)
    return answer
n,m=map(int,input().split())
print(solution(n,m))