def solution(arr1, arr2):
    res = []
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    for r in range(r1):  # 3
        line = []
        for c_2 in range(c2):  # 2
            mul = 0
            for c_1 in range(c1):
                mul += arr1[r][c_1] * arr2[c_1][c_2]

            line.append(mul)
        res.append(line)
    return res

arr1=[[1,4],[3,2],[4,1]]
arr2=[[3,3],[3,3]]
print(solution(arr1,arr2))


