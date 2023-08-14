from itertools import combinations

def solution(num):
    answer=0
    perm=list(combinations(num,3))
    for i in perm:
        if sum(i)==0:
            answer+=1

    return answer

# 3명의 정수 번호를 더했을때 0이 되면 3명은 삼총사
# ex) -2,3,0,2,-5 //// -2+0+2 or 3+2-5 -> 삼총사

num=[-2,3,0,2,-5]
perm=list(combinations(num,3))
cnt=0
for i in perm:
    if sum(i)==0:
        cnt+=1
print(cnt)