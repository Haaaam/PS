'''prices=[1,2,3,2,3]
time=[]
answer=[0]*len(prices)

for i in range(len(prices)):
    while time and prices[time[-1]]>prices[i]:
        tmp=time.pop()
        answer[tmp]=i-tmp
    time.append(i)
while time:
    tmp=time.pop()
    answer[tmp]=len(prices)-tmp-1
print(answer)'''


def solution(prices):
    answer = [0] * len(prices)
    time = []
    for i in range(len(prices)):
        while time and prices[time[-1]] > prices[i]:
            tmp = time.pop()
            answer[tmp] = i - tmp
        time.append(i)
    while time:
        tmp = time.pop()
        answer[tmp] = len(prices) - tmp - 1

    return answer
