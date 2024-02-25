# s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

# s는 길이 1 이상 200 이하인 문자열입니다.
# s는 알파벳과 숫자, 공백문자로 이루어져 있습니다.
# 숫자는 단어의 첫 문자로만 나옵니다.
# 숫자로만 이루어진 단어는 없습니다.
# 공백문자가 연속해서 나올 수 있습니다.

def solution(s):
    answer = ''
    s=s.split(' ')
    for i,j in enumerate(s):
        s[i]=j[:1].upper()+j[1:].lower()
    return " ".join(s)

s="3people unFollowed me"
print(solution(s))