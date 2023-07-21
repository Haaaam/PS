def solution(price, money, count):

    res=sum(price*i for i in range(1,count+1))
    if res>money:
        return res-money
    else:
        return 0

