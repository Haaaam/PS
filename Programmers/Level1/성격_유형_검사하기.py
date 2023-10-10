def solution(survey, choices):
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    answer = ''

    # 4를 기준으로 둘중 하나의 성격으로 분류되기때문에 choices-4 or 4-choices
    for s, c in zip(survey, choices):
        if c > 4:
            score[s[1]] += (c - 4)
        elif c < 4:
            score[s[0]] += (4 - c)

    score = list(score.items())
    print(score)
    for i in range(0, 8, 2):

        if score[i][1] >= score[i + 1][1]:
            answer += score[i][0]
        else:
            answer += score[i + 1][0]
    return answer


# 지표 번호
# 1번 지표(R,T) 2번 지표: (C,F), 3번 지표: J, M, 4번 지표: A,N

# 성격유형은 총 16가지가 나올 수 있음
# 매우 비동의 네오형 3, 비동의 네오형 2, 약간 비동의 네오형 1, 모르겠음 0,
# 약간 동의 어피치형 1, 동의 어피치형 2, 매우 동의 어피치형 3

survey=["AN", "CF", "MJ", "RT", "NA"]
choices=[5, 3, 2, 7, 5]
score={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
answer=''

for s,c in zip(survey,choices):
    if c>4: score[s[1]]+=(c-4)
    elif c<4: score[s[0]]+=(4-c)


score=list(score.items())
print(score)
for i in range(0,8,2):

    if score[i][1]>=score[i+1][1]:
        answer+=score[i][0]
    else:
        answer+=score[i+1][0]
print(answer)


