# 문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서 자신과 가장 가까운 곳에 있는
# 글자가 어디 있는지 알고 싶다.


def solution(s):
    answer,res=[],{}
    for i in range(len(s)):
        if s[i] not in res:
            answer.append(-1)
        else:
            answer.append(i-res[s[i]])
        res[s[i]]=i
    return answer

s="banana"
print(solution(s))
