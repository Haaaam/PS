def solution(answers):
    student=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    answer,check=[],[]

    for s in range(len(student)):
        problem=[]
        for i in range(len(answers)):
            if answers[i]==student[s][i%len(student[s])]:
                problem.append(True)

        check.append(len(problem))

    winner=max(check)
    for i in range(len(check)):
        if check[i]==winner:
            answer.append(i+1)
    return answer

answers=[1,2,3,4,5]
# return 가장 많은 문제를 맞춘사람
# 가장 높은 점수를 받은 사람이 여럿일 경우, return 하는 값을 오름차순 정렬
# 수포자 3명

student=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]

answer,check=[],[]

for s in range(len(student)):
    problem=[]
    for i in range(len(answers)):
        if answers[i]==student[s][i%len(student[s])]:
            problem.append(True)

    check.append(len(problem))
"""
answer,check=[],[0]*3
for i in range(len(answers)):

    if answers[i]==student[0][i%len(student[0])]:
        check[0]+=1

    if answers[i]==student[1][i%len(student[1])]:
        check[1]+=1

    if answers[i]==student[2][i%len(student[2])]:
        check[2]+=1

"""

for i in range(len(check)):
    if check[i]==max(check):
        answer.append(i+1)
print(answer)