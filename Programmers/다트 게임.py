def solution(dartResult):
    s=[]
    res=''
    for i in dartResult:
        if i.isdigit():
            res += i
        elif i == 'S':
            s.append(int(res) ** 1)
            res = ''
        elif i == 'D':
            s.append(int(res) ** 2)
            res = ''
        elif i == 'T':
            s.append(int(res) ** 3)
            res = ''
        elif i == '*':
            if len(s) > 1:
                s[-2] *= 2
            s[-1] *= 2
        elif i == '#':
            s[-1] *= (-1)

    return sum(s)

print(solution('1S2D*3T'))




