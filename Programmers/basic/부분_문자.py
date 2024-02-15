# str1이 str2의 부분 문자열이라면 1을 부분 문자열이 아닌 0을 return 하도록

def solution(str1,str2):

    if str1 in str2:
        return 1
    return 0

str1="abc"
str2="aabcc"
print(solution(str1,str2))