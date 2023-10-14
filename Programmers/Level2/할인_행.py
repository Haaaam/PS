# 할인 행사
def solution(want,number,discount):
    answer = 0
    dic = dict()
    for i in range(len(want)):
        dic[want[i]] = number[i]
    n = 0
    while 10 + n <= len(discount):
        for i in range(len(want)):
            dic[want[i]] = number[i]

        for i in range(n, 10 + n):
            if discount[i] in dic and dic[discount[i]] > 0:
                dic[discount[i]] -= 1

        if sum(dic.values()) <= 0:
            answer += 1

        n += 1
    return answer

# XYZ 마트는 10일동안 회원 자격 부여
# 회원을 대상으로 매일 한 가지 제품을 할인하는 행사 진행
# 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰 회원가입
# want: 정현이가 원하는 제품, number: 제품의 수량을 나타내는 정수 배열
# discount: XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열
# return: 할인 받을 수 있는 회원등록 날짜의 총 일수
# 없으면 0을 return
want=["banana","apple","rice","pork","pot"]
number=[3,2,2,2,1]
discount=["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

answer=0
dic=dict()
for i in range(len(want)):
    dic[want[i]]=number[i]
n=0
while 10+n<=len(discount):
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(n,10+n):
        if discount[i] in dic and dic[discount[i]]>0:
            dic[discount[i]]-=1

    if sum(dic.values())<=0:
        answer+=1

    n+=1
print(answer)