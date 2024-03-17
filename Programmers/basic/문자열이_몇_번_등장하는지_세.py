# 문자열 myString과 pat이 주어진다. myString에서 pat이 등장하는 횟수를 return하는 solution 함수 완성하기
def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        if myString[i:i+len(pat)]==pat:
            answer+=1


    return answer
myString="banana"
pat="ana"
print(solution(myString,pat))