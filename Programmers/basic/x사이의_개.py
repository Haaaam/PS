def solution(myString):
    myString = myString.split("x")

    answer = []
    for i in myString:
        answer.append(len(i))
    return answer

# x 사이의 개수
myString="oxooxoxxox"
myString=myString.split("x")

answer=[]
for i in myString:
    answer.append(len(i))
print(answer)
