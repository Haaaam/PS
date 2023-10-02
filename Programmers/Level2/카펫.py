# 완전 탐색
def solution(brown, yellow):
    # rc=yellow_brown
    # (r-2)*(c-2)=yellow
    all = yellow + brown

    # 초기 가능한 r,c 값 설정
    r, c = 3, 1

    while 1:
        # 높이: all//r
       # c = all // r
        # 나머지: all%r
       # remainder = all % r
        c,remainder=divmod(all,r)
        
        if remainder == 0 and r >= c and (r - 2) * (c - 2) == yellow:
            return [r, c]

        else:
            r += 1
    #while r*c !=all:


    # 런타임 에러남
    """
    for i in range(1, int(all ** (1 / 2)) + 1):
        if (all) % i == 0:
            answer.append(i)
            if all // i not in answer:
                answer.append(all // i)
    answer = sorted(answer)
    if all % 2 == 0:
        r = answer[:len(answer) // 2 - 1:-1]
        c = answer[:len(answer) // 2]
    else:
        r = answer[:len(answer) // 2 - 1:-1]
        c = answer[:len(answer) // 2 + 1]

    for i in range(len(r)):
        if r[i] * c[i] == all and (r[i] - 2) * (c[i] - 2) == yellow:
            return [r[i],c[i]]
    """
brown,yellow=24,24

print(solution(brown,yellow))

"""
def f(all):
    answer=[]
    for i in range(1,int(all**(1/2))+1):
        if (all)%i==0:
            answer.append(i)
            if all // i not in answer:
                answer.append(all // i)
    return sorted(answer)

def solution(brown, yellow):

    all = yellow + brown

    answer=f(all)

    if all % 2 == 0:
        r = int(len(answer) / 2)
        c = int(len(answer) / 2) -1
    else:
        r = int(len(answer) /2)
        c = int(len(answer) / 2)

    while 1:
        if (answer[r] - 2) * (answer[c] - 2) == yellow:
            return [answer[r],answer[c]]
        else:
            r+=1
            c-=1


# 갈색 격자의 수: brown
# 노란색 격자의 수: yellow
brown,yellow=24,24

print(solution(brown,yellow))

"""
