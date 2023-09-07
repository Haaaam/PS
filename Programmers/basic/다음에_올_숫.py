def solution(common):
    answer=0
    return answer

common=[2,4,8]
answer=0
#등차인 경우
if common[1]-common[0] == common[2]-common[2]:
    answer=common[-1]+(common[1]-common[0])
# 등비인 경우
else:

    answer=common[-1]*(common[-1]//common[-2])

print(answer)