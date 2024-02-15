# programmers-962 행성에서는 나이를 알파벳으로 말하고 있다.
# a는 0, b는 1, c는 2, ...,j는 9
# return PROGRAMMER-962식 나이

def solution(age):

    answer = ''
    age_dict={'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}

    for i in str(age):
        answer+=age_dict[i]

    return answer
age=23
print(solution(age))