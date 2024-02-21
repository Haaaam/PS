# 숫자의 일부 자릿수를 영단어로 바꾸는 예시
# 1478-> "one4seveneight"
# 234567 -> "23four5six7"
# 10203 -> "1zerotwozero3"

"""
def solution(s):
    answer=''
    dict={"zero":'0',"one":'1',"two":'2',"three":'3',"four":'4',"five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9'}
    tmp=''

    for i in s:
        tmp+=i
        if tmp in dict:
            answer+=dict[tmp]
            tmp=''

        elif tmp.isdigit():
            answer+=str(tmp)
            tmp=''


    return int(answer)
"""
# 다른 사람의 짧은 코드
def solution(s):
    answer=s
    dict = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7',
            "eight": '8', "nine": '9'}
    # dictionary의 replace 활용하여 s의 key값을 value로 변환
    for key,value in dict.items():
        answer=answer.replace(key,value)
    return int(answer)
s="one4seveneight"
print(solution(s))