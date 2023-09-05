# 상위 k번째 이내이면 해당 가수의 점수를 명예의 전당이라는 목록에 올려 기념
# k일 다음부터 출연 가수의 점수가 기존의 명예의 전당 목록의 k번째 순위의 가수 점수보다 높으면
# 출연 가수의 점수가 명예의 전당에 오르고 k번쨰 순위의 점수는 명예의 전당에서 내려온다
def solution(k, score):
    answer=[]
    res=[]
    for i in range(len(score)):
        answer.append(score[i])
        answer=sorted(answer,reverse=True)
        if len(answer)>k:

            answer.pop()
        res.append(answer[-1])
    return res

answer=[]
k=3
score=[10,100,20,150,1,100,200]
res=[]
for i in range(len(score)):
    answer.append(score[i])
    answer=sorted(answer,reverse=True)
    if len(answer)>k:

        answer.pop()
    res.append(answer[-1])
print(res)
