# 학생들의 번호는 체격 순으로 매겨져 있다.
# 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있따.
# n: 전체 학생의 수, lost: 체육복을 도난당한 학생들의 번호가 담긴 배열,
# reserve: 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열
# return 체육수업을 들을 수 있는 학생의 최댓값
def solution(n,lost,reserve):

    answer=0
    lost,reserve=sorted(lost),sorted(reserve)

    for i in range(1,n+1):
        # 체육복을 안 잃어 버린 경우
        if i not in lost:
            answer+=1
        # 여벌의 체육복이 있는 경우
        # 잃어버린 학생들 중 여벌의 체육복이 있는 경우도 고려
        elif i in reserve:
            answer+=1
            reserve.remove(i)
            lost.remove(i)

    # 여벌의 체육복도 없는 경우
    for i in lost:
        if i-1 in reserve:
            answer+=1
            reserve.remove(i-1)
        elif i+1 in reserve:
            answer+=1
            reserve.remove(i+1)


    return answer


n=5
lost=[4,2]
reserve=[5,3]
print(solution(n,lost,reserve))
