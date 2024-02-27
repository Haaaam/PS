# 사과는 상태에 따라 1점부터 k점까지의 점수로 분류
# k점이 최상품의 사과이고 1점이 최하품의 사과
# 사과 한 상자의 가격:
# - 한 상자에 사과를 m개씩 담아 포장합니다.
# - 상자에 담긴 사과 중 가장 낮은 점수가 p(1<=p<=k)점인 경우,
# 사과 한 상자의 가격은 p*m입니다.
# 가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익을 계산하고자 합니다.
def solution(k,m,score):
    answer=0
    score=sorted(score,reverse=True) # 내림차순으로 정렬
    # 한 상자에 담을 수 있는 사과 m개씩 확인하여 최대 이익 구하기
    for i in range(0,len(score),m):
        # 사과 1상자를 만들 수 있는 경우
        if i+m<=len(score):
            answer+=min(score[i:i+m])*m
        # 사과 1상자 만들 수 없는 경우, 남는 사과 버리기
        else:
            break
    return answer

k,m=3,4
score=[1,2,3,1,2,3,1]
print(solution(k,m,score))