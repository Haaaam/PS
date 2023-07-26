def solution(n):
    answer=sorted([int(i) for i in str(n)], reverse=True)
    res=''
    for i in answer: res+=str(i)
    return int(res)
n=118372
print(solution(n))
