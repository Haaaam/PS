def solution(n):
    arr=reversed([i for i in str(n)])

    return [int(i) for i in arr]

n=12345
print(solution(n))

#for i in range(len(str(n))):
