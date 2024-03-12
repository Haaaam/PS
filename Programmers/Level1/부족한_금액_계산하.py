# 이 놀이 기구의 원래 이용료는 price,
# 놀이기구를 n번째 이용한다면 원래 이용료의 n배를 받기로 함
# return 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지
def solution(price,money,count):

    tmp=0
    for i in range(1,count+1):
        tmp+=price*i

    if money-tmp<0:
        return tmp-money
    else:
        return 0


price,money,count=3,20,4

print(solution(price,money,count))