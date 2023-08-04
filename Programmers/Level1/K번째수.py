def solution(array, commands):
    res = []
    for i in range(len(commands)):
        f,l,k=commands[i][0],commands[i][1],commands[i][-1]
        array_new=sorted(array[f-1:l])
        res.append(array_new[k-1])
    return res

array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array,commands))