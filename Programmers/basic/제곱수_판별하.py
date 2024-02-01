import math
def solution(n):
    answer=math.sqrt(n)
    if (answer).is_integer():
        return 1
    else:
        return 2
