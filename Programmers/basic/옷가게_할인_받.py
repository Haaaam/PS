def solution(price):
    answer = 0
    return answer

# 머쓱이네 옷가게는 10만원 이상 사면 5%, 30만원 이상 10%, 50만원 이상 20%
# price가 주어질때, 지급해야할 금액

price=580000
answer=0
if price>=500000:
    price-=(price*0.2)
elif price>=300000:
    price-=(price*0.1)
elif price>=100000:
    price-=(price*0.05)
print(int(price))













