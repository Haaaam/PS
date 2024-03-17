# 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있다.
# 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 한다.
# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴
# 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return하도록 solution 함수를 작성할 것

# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수도 있다.
def solution(n, lost, reserve):
    answer = 0
    # 체육복이 있는 학생들
    lost,reserve=sorted(lost),sorted(reserve)
    for i in range(1,n+1):
        # 체육복을 잃어버리지 않은 경우
        if i not in lost:
            answer+=1
        # 여벌 체육복을 가져왔는데 체육복을 도난당한 경우
        elif i in reserve:
                answer+=1
                reserve.remove(i)
                lost.remove(i)
    # 여벌 체육복 없는 경우
    for i in range(1,n+1):
        if i in lost:
            if i-1 in reserve:
                answer+=1
                reserve.remove(i-1) # 빌려줬으므로 i-1을 reserve에서 제거
            elif i+1 in reserve:
                answer+=1
                reserve.remove(i+1) # 빌려줬으므로 i+1을 reserve에서 제거

    return answer

n=5
lost=[2,4]
reserve=[3]
print(solution(n,lost,reserve))