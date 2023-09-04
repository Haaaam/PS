def solution(food):
    res = ''
    for i in range(len(food)):
        res += str(i) * (food[i] // 2)


    return res+"0"+res[::-1]

food=[1, 7, 1, 2]
print(solution(food))
