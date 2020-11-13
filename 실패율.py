def solution(N,stages):
    answer=[]
    l=len(stages)
    for i in range(1,N+1):
        cnt = stages.count(i)
        if l == 0:  # 스테이지에 도달한 유저가 없는 경우
            fail = 0
        else:
            fail = cnt / l
        answer.append((i, fail))
        l -= cnt
    answer=sorted(answer, key=lambda i:i[1], reverse=True)

    return [i[0] for i in answer]
N=int(input())
stages=list(map(int,input().split()))
print(solution(N,stages))


