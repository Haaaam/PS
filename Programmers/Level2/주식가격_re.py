# 주식가격
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return

def solution(prices):
    time=[0]*len(prices)
    for i in range(len(prices)-1):
        for j in range(i,len(prices)-1):
            if prices[j]>=prices[i]:
                time[i]+=1
            else:
                break

    return time
prices=[1,2,3,2,3]
print(solution(prices))
