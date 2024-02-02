# 등수 매기기
def solution(score):
    answer=[]
    avg=[]
    for i in score:
        avg.append(sum(i)//len(i))
    avg_sort=sorted(avg,reverse=True)

    for i in avg:
        answer.append(avg_sort.index(i)+1)

    return answer


score=[[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
print(solution(score))