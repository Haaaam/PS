# 자릿수 더하기
def solution(n):
    n=str(n)
    res=0
    for i in n: res+=int(i)

    return res
N=123
print(solution(N))
