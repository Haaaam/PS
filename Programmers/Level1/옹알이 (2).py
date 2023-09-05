def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for i in babbling:
        word=''
        a=''
        cnt=0
        for j in i:
            word+=j

            if word in words and word!=a:
                a=word
                word=''
                cnt+=1
            elif word==a:

                a=''
                cnt=0
            else:
                cnt=0

        if  cnt>0:

            answer+=1

    return answer



babbling=		["aya", "yee", "u"]



print(solution(babbling))