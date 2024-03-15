# 두 정수 X,Y의 임의의 자리에서 공통으로 나타나는 정수 k들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 한다.
# X,Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1
# X,Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0
# X,Y가 주어졌을 때, X,Y의 짝꿍을 return하는 solution함수 완성
def solution(X,Y):
    answer=''
    # 공통으로 나타나는 숫자 찾기
    for i in range(9,-1,-1):
        answer+=(str(i)*min(X.count(str(i)),Y.count(str(i))))
    # 짝꿍이 존재하지 않을 경우
    if answer=='':
        return "-1"
    # 짝꿍이 존재할 경우
    else:
        # 가장 큰 정수 return위해 내림차순 정렬
        answer=sorted(answer,reverse=True)
        # 짝꿍이 0으로만 구성되어 있을 경우
        if answer[0]=="0":
            return "0"
        else:
            return ''.join(answer)

X="100"
Y="123450"
print(solution(X,Y))