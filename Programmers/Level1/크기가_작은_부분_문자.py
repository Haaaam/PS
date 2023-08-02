def solution(t,p):
    res=0
    for i in range(len(t)):
        if len(t[i:i+len(p)]) !=len(p):
            break
        if t[i:i+len(p)] <=p:
            res+=1

    return res

t="10203"
p="15"
print(solution(t,p))

