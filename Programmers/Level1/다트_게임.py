def solution(dartResult):
    s=[]
    res=''
    for i in dartResult:
        if i.isdigit():
            res += i
        else:
            if i == "S":
                s.append(int(res) ** 1)
                res = ''
            elif i == "D":
                s.append(int(res) ** 2)
                res = ''
            elif i == "T":
                s.append(int(res) ** 3)
                res = ''
            if i == "*":
                if len(s) > 1:
                    s[-2] *= 2
                    s[-1] *= 2
                elif len(s)<=1:
                    s[-1]*=2
            elif i == "#":
                s[-1] = -s[-1]
    return sum(s)

dartResult="1S2D*3T"
answer=0
s=[]
res=''
# 점수 계산 로직
# 다트 게임은 총 3번의 기회로 구성
# 각 기회마다 얻을 수 있는 점수는 0~10
# *: 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다
# #: 아차상 당첨시 해당 점수는 마이너스
# S: 1제곱, D: 2제곱, T: 3제곱
for i in dartResult:
    if i.isdigit():
        res+=i
    else:
        if i=="S":
            s.append(int(res)**1)
            res=''
        elif i=="D":
            s.append(int(res)**2)
            res=''
        elif i=="T":
            s.append(int(res)**3)
            res=''
        if i=="*":
            if len(s)>1:
                s[-2]*=2
                s[-1]*=2
            elif len(s) <= 1:
                s[-1] *= 2
        elif i=="#":
            s[-1]= -s[-1]
print(sum(s))


