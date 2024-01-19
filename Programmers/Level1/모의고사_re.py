# 수포자 삼인방 모의고사 수학문제 전부 찍으려 한다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오른차순으로 정렬
def solution(answers):
    answer=[]
    students=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    check=[0]*len(students)
    for i in range(len(students)):
        for j in range(len(answers)):
            # 문제는 최대 10000문제이고 수포자들은 반복해서 찍기때문에 답안의 j번째%len(students[i]로 해서
            # 답안과 비교하기기            if answers[j]==students[i][j%len(students[i])]:
                check[i]+=1


    for i in range(len(check)):
        if check[i]==max(check):
            answer.append(i+1)
    return answer

answers=[1,2,3,4,5]
print(solution(answers))