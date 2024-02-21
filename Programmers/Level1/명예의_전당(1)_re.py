# 매일 출연한 가수의 점수가 지금까지 출연 가수들의 점수 중 상위 k번째 이내이면
# 해당 가수의 점수를 명예의 전당이라는 목록에 올려 기념한다.
# 프로그램 시작 이후 초기에는 k일까지는 모든 출연 가수의 점수가 명예의 전당에 오른다.
# k일 다음부터는 출연 가수의 점수가 기존 명예의 전당 목록의 k번째 순위의 가수 점수보다 더 높으면,
# 출연 가수의 점수가 명예의 전당에 오르게 되고 기존의 k번째 순위의 점수는 명예의 전당에서 내려오게 된다.
# k: 명예의 전당 목록의 점수의 개수, score: 1일부터 마지막 날까지 출연한 가수들의 점수
# return 매일 발표된 명예의 전당의 최하위 점수

def solution(k, score):
    answer = []
    tmp=[]
    for i in range(len(score)):
        print(tmp)
        tmp.append(score[i])
        tmp=sorted(tmp,reverse=True)

        if len(tmp)>k:
            tmp.pop()

        answer.append(tmp[-1])

    return answer

k=3
score=[10, 100, 20, 150, 1, 100, 200]
print(solution(k,score))