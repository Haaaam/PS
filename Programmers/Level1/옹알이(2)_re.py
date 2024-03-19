# 머쓱이는 태어난 지 11개월 된 조카를 돌보고 있다.
# 조카는 "aya", "ye", "woo", "ma" 네가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 못한다.
# 연속해서 같은 발음을 하는 것을 어려워 한다.
# return 머쓱이의 조카가 발음할 수 있는 단어의 개수
# 네 가지를 붙여 만들 수 있는 발음 이외에는 어떤 발음도 할 수 없는 것으로 규정한다.

def solution(babbling):
    answer=0
    say=["aya","ye","woo","ma"]

    for bab in babbling:
        word=''
        tmp=''
        cnt=0

        for j in bab:
            word+=j
            # word가 say에 있고 동일한 말을 반복하지 않았을 경우 cnt+1
            if word in say and word!=tmp:

                tmp=word
                word=''
                cnt+=1
            # 동일한 말을 반복했을 경우
            elif word==tmp:
                tmp=''
                cnt=0
            else:
                cnt=0
        if cnt>0:
            answer+=1

    return answer


babbling=["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))