def solution(num, total):
    res=[i for i in range(num)]

    while sum(res)<total and len(res)<=num:
        if sum(res)<total:
            res.pop(0)
            res.append(res[-1]+1)
    if sum(res)>total and len(res)<=num:
        res.pop(res[-1])
        res.append(-1)
    return sorted(res)

num=5
total=5

print(solution(num,total))
