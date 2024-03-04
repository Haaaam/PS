# 사전에 알파벳 모음 'A','E','I','O','U'만을 사용하여 만들 수 있는,
# 길이 5 이하의 모든 단어가 수록되어 있다.
# 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"이다.
# 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성하시오.

# 참고 블로그
# https://yongs-0a.tistory.com/entry/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%97%B0%EC%8A%B5-%EC%99%84%EC%A0%84%ED%83%90%EC%83%89-%EB%AA%A8%EC%9D%8C%EC%82%AC%EC%A0%84


def solution(word):
    answer = 0
    cal=[781,156,31,6,1]
    dict="AEIOU"
    for i in range(len(word)):

        answer+=dict.find(word[i])*cal[i]+1
    return answer

word="EIO"
print(solution(word))