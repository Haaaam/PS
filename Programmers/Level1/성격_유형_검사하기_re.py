# survey의 원소: "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"
# ["매우 비동의": 네오형 3점, "비동의": 네오형 2점, "약간 비동의": 네오형 1점, "모르겠음": "어떤 성격 유형도 점수를 얻지 않습니다"
# , "약간 동의": 어피치형 1점, "동의": 어피치형 2점, "매우 동의": "어피치형 3점"]
# 검사 결과는 모든 질문의 성격 유형 점수를 더하여 각 지표에서 더 높은 점수를 받은 성격 유형이 검사자의 성격 유형
# 단, 하나의 지표에서 각 성격 유형 점수가 같으면, 두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라 판단
# 검사자의 성격 유형 검사 결과를 지표 번호 순서대로 return
def solution(survey,choices):
    answer=''
    mbti={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(choices)):
        a,b=survey[i][0],survey[i][1] # survey 선택 유형 나누기
        if choices[i]>4:
            mbti[b]+=abs(4-choices[i])
        elif choices[i]<4:
            mbti[a]+=abs(4-choices[i])

    mbti=list(mbti.items()) # dictionary를 list형태로 변형
    for i in range(0,len(mbti),2):
        if mbti[i][1]>=mbti[i+1][1]:
            answer+=mbti[i][0]
        else:
            answer+=mbti[i+1][0]

    return answer

survey=["AN","CF","MJ","RT","NA"]
choices=[5,3,2,7,5]
print(solution(survey, choices))
