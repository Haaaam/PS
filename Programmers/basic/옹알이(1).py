def solution(babbling):
    answer = 0
    for i in babbling:
        word = ''
        cnt = 0
        for j in i:
            word += j
            if word in check:
                cnt += 1
                word = ''
            else:
                cnt = 0
        if cnt > 0:
            answer += 1
    return answer

babbling=["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
check=["aya","ye","woo","ma"]

answer=0


for i in babbling:
    word=''
    cnt=0
    for j in i:
        word+=j
        if word in check:
            cnt+=1
            word=''
        else:
            cnt=0
    if cnt>0:
        answer+=1


print(answer)



