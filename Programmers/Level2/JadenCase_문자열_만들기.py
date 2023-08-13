#def solution(s):
#    res = []
#    s = list(s.split())
#    for i in s:
#        try:
#            if int(i[0]):
#                res.append(i)
#        except:
#            if len(i)!=0:
#                ans = ''
#                ans += i[0].upper()
#                ans += i[1:].lower()
#                res.append(ans)
#        else: pass
#    return " ".join(res)

def solution(s):
    sen = s.split(" ")

    for i, j in enumerate(sen):
        sen[i] = j[:1].upper() + j[1:].lower()
    return " ".join(sen)
s="3people  unFollowed me"
print(solution(s))