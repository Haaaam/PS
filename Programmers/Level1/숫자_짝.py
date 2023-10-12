def solution(X,Y):

    answer = ''
    for i in range(9,-1,-1):
        answer+=(str(i)*min(X.count(str(i)),Y.count(str(i))))

    # 시간초과 나서 위의 코드로 수정함.
    """
    if x_l <= y_l:
        for i in X:
            if i in Y and tmp.count(i) < Y.count(i):
                tmp.append(i)
    else:
        for i in Y:
            if i in X and tmp.count(i) < X.count(i):
                tmp.append(i)
    """
    # 짝꿍이 존재하지 않는 경우
    if not answer:
        answer = "-1"
    else:
        answer = sorted(answer, reverse=True)
        # for i in sorted(tmp,reverse=True):
        #    answer+=i
        if answer[0] == "0":
            return "0"
    return ''.join(answer)
# 정수 k들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 한다.
# X,Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1
# X,Y의 짝꿍이 0으로만 구성되어 있다면 짝꿍은 0
X,Y="12321","42531"

answer=''
for i in range(9,-1,-1):
    answer+=(str(i)*min(X.count(str(i)),Y.count(str(i))))

    # 짝꿍이 존재하지 않는 경우
if not answer:
    answer="-1"
else:
    answer=sorted(answer,reverse=True)
    #for i in sorted(tmp,reverse=True):
    #    answer+=i
    if answer[0]=="0":
        answer="0"

print(''.join(answer))


