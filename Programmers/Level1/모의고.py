# 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
# 1번: 1,2,3,4,5,1,2,3,4,5,,,,
# 2번: 2,1,2,3,2,4,2,5,2,1,2,3,2,4,2,5,,,,
# 3번: 3,3,1,1,2,2,4,4,5,5,3,3,1,1,,,,,,
# 시험은 최대 10,000 문제로 구성
# 문제의 정답은 1,2,3,4,5 중 하나
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순으로 정렬하기
def solution(answers):

    problem=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    tmp = [0] * len(problem)
    answer=[]


    for j in range(len(problem)):
        for i in range(len(answers)):
            # 각 수포자학생의 반복되는 답의 길이만큼 i%len(problem[j])를 해준다. 런타임에러 방지
            if problem[j][i%len(problem[j])]==answers[i]:
                tmp[j]+=1

    # 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순으로 정렬
    for i in range(len(tmp)):
        if tmp[i]==max(tmp):
            answer.append(i+1)

    return answer

answers=[1,3,2,4,2]
print(solution(answers))