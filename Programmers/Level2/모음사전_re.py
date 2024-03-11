# 사전에 알파벳 모음 'A','E','I','O','U' 만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있다.
# 첫번째 단어는 "A", 그 다음 단어는 "AA"이며, 마지막 단어는 "UUUUU"
# [781,156,31,6,1]
def solution(word):
    answer = 0
    dic=[781,156,31,6,1]
    dict="AEIOU"
    for i in range(len(word)):
        answer+=(dict.find(word[i])*dic[i]+1)


    return answer

word="AAAE"
print(solution(word))