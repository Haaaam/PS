def solution(sides):

    sides=sorted(sides)
    if sum(sides[:-1])>sides[-1]:
        return 1
    else:
        return 2


sides=[199,72,222]
print(solution(sides))