# 가장 가까운 같은 글자
def solution(s):
    answer=[]
    s=list(s)
    for i in range(len(s)):
        if s[i] not in res:
            answer.append(-1)
            res[s[i]]=i
        elif s[i] in res:

            answer.append(i-res[s[i]])
            res[s[i]]=i
    return answer

s="banana"
s=list(s)
answer=[]
res={}
for i in range(len(s)):
    if s[i] not in res:
        answer.append(-1)
        res[s[i]]=i
    elif s[i] in res:

        answer.append(i-res[s[i]])
        res[s[i]]=i

print(answer)
