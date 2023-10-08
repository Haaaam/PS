def solution(strings, n):

    return sorted(strings, key= lambda x:(x[n],x))

strings=["sun","bed","car"]
n=int(input())

print(solution(strings,n))