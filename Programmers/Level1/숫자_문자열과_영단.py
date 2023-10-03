def solution(s):
    dict={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    tmp = ''
    answer = ''
    for i in s:
        tmp += i
        if tmp in dict:
            answer += str(dict[tmp])
            tmp = ''
        elif tmp.isnumeric(): # 주어진 문자열이 숫자로 되어있는지 검사(str.isnumeric())
            answer += str(tmp)
            tmp = ''
    return answer
"""
# 다른 사람 풀이
각 문자열에 해당하는 숫자도 string 형태로 변형하여 문자열을 해당하는 숫자로 바꿔주면 됐음(replace)...
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
"""

dict={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

s="one4seveneight"
tmp=''
answer=''
for i in s:
    tmp+=i
    if tmp in dict:
        answer+=str(dict[tmp])
        tmp=''
    elif tmp.isnumeric():
        answer+=str(tmp)
        tmp=''

print(answer)