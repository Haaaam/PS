def solution(price,money,count):

    res = sum([price * i for i in range(1, count + 1)])
    if money - res > 0:
        return 0
    else:
        return res - money


price,money,count=3,20,4

print(solution(price,money,count))
