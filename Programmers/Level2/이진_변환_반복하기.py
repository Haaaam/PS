def solution(s):

    cnt0 = 0
    cnt2 = 0

    while s != '1':

        cnt2 += 1
        cnt0 += s.count('0')
        s = s.split('0')
        tmp = ''
        for i in s:
            tmp += i
        s = str(bin(len(tmp)))[2:]
    return [cnt2,cnt0]
# 이진 변환의 횟수, 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return
s="01110"


print(solution(s))
# 2진법 변환

# x의 모든 0을 제거한다.
# x의 길이를 c 2진법으로 표현한 문자열

