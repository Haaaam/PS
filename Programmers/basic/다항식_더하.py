def solution(polynomial):
    res = []
    polynomial=polynomial.split(' ')
    polynomial=list(polynomial)
    ans = 0
    for i in polynomial:
        if 'x' in i:
            if len(i) == 1:
                res.append(1)
            else:
                i = i.split('x')
                res.append(int(i[0]))

        elif i != '+':
            ans += int(i)
    if len(res)!=0 and ans!=0:
        if len(res)==1 and 1 in res:
            return f"x + {ans}"
        return f"{str(sum(res))}x + {ans}"
    elif len(res)==0:
        return f"{ans}"
    elif len(res)==1 and 1 in res:
        return f"x"
    else:
        return f"{str(sum(res))}x"
polynomial="x + 1"

print(solution(polynomial))
