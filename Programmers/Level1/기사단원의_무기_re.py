# 숫자나라 기사단의 각 기사에게는 1번부터 number까지 번호가 지정되어 있다.
# 각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매하려 한다.
# 공격력의 제한수치를 정하고, 제한수치보다 큰 공격력을 가진 무기를 구매해야 하는 기사는
# 협약기관에서 정한 공격력을 가지는 무기를 구매해야 한다.
# 무기를 만들 때, 무기의 공격력 1당 1kg의 철이 필요하다.
# number: 기사단원의 수
# limit: 이웃나라와 협약으로 정해진 공격력의 제한수치를 나타내는 정수
# power: 제한수치를 초과한 기사가 사용할 무기의 공격력을 나타내는 정수
# 필요한 철의 무게 return

def solution(number, limit, power):
    answer = 0
    numbers=[]
    # 약수의 갯수 구하기
    for i in range(1,number+1):
        cnt=0
        # 제곱근을 사용하여 for문 돌리기
        for j in range(1,int(i**(1/2))+1):
            if (i%j==0):
                cnt+=1

                if j**2!=i:
                    cnt+=1
        numbers.append(cnt)

    for i in range(len(numbers)):
        # 공격력이 limit을 넘지 않을 경우
        if numbers[i]<=limit:
            answer+=numbers[i]
        # 공격력이 limit을 넘을 경우 power를 더한다.
        else:
            answer+=power

    return answer
number=5
limit=3
power=2
print(solution(number,limit,power))
