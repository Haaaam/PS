def solution(name, yearning, photo):
    dic = dict()
    answer = []
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for idx in range(len(photo)):
        cnt = 0
        for n in photo[idx]:
            if n in dic:
                cnt += dic[n]
            else:
                continue
        answer.append(cnt)

    return answer

name=["may","kein","kain","radi"]
yearning=[5,10,1,3]
photo=[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

dic=dict()
answer=[]
for i in range(len(name)):
    dic[name[i]]=yearning[i]
for idx in range(len(photo)):
    cnt=0
    for n in photo[idx]:
        if n in dic:
            cnt+=dic[n]
        else:
            continue
    answer.append(cnt)
print(answer)