def solution(n,lost,reserve):
    answer=0
    return answer

n=int(input()) # 전체 학생 수
lost=sorted(map(int,input().split())) #잃어버린 학생
reserve=sorted(map(int,input().split())) # 여벌 체육복 가져온 학생

ans=0
for i in range(1,n+1):
    if i not in lost:
        ans+=1 # 1 3 5

    elif i in reserve: # lost와 reserve에 똑같은 숫자가 있으면 제거
        ans+=1

        reserve.remove(i)
        lost.remove(i)

for i in lost: # 2 4
    print(i)
    if i-1 in reserve:
        ans+=1
        reserve.remove(i-1)
    elif i+1 in reserve:
        ans+=1
        reserve.remove(i+1)



print(ans)

"""
# 정답
def solution(n, lost, reserve):
    ans = 0
    lost=sorted(lost)
    reserve=sorted(reserve)
    for i in range(1,n+1):
        if i not in lost:
            ans+=1
        elif i in reserve:
            ans+=1
            reserve.remove(i)
            lost.remove(i)
    for i in lost:
        if i-1 in reserve:
            ans+=1
            reserve.remove(i-1)
        elif i+1 in reserve:
            ans+=1
            reserve.remove(i+1)
    return ans
"""