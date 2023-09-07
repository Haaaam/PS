def solution(quiz):
    answer=[]
    for s in quiz:
        s = s.split(' ')
        x = s[0]
        y = s[2]
        res = 0
        if s[1] == '-':
            res = int(x) - int(y)
        else:
            res = int(x) + int(y)

        if str(res) == s[-1]:
            answer.append('O')
        else:
            answer.append('X')
    return answer
quiz=["3 - 4 = -3", "5 + 6 = 11"]
answer=[]
for s in quiz:
    s=s.split(' ')
    x=s[0]
    y=s[2]
    res=0
    if s[1]=='-':
        res=int(x) - int(y)
    else:
        res=int(x) + int(y)

    if str(res)==s[-1]:
            answer.append('O')
    else:
        answer.append('X')
print(answer)




