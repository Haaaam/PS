def solution(land):
    answer=0
    return answer

# 땅따먹기 게임의 땅은 총 N행 4열로 이루어져 있다.
# 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 한다.
# 단, 한 행씩 내려올 때, 같은 열을 연속해서 밝을 수 없다.

land=[[1,2,3,5],[5,6,7,8],[4,3,2,1]]
n=len(land) # n행
# 누적 방식으로 풀이
# land[i][j]=i행 j열에서 점수의 최대값
for i in range(1,len(land)):
    land[i][0]+=max(land[i-1][1],land[i-1][2],land[i-1][3])
    land[i][1]+=max(land[i-1][0],land[i-1][2],land[i-1][3])
    land[i][2]+=max(land[i-1][0],land[i-1][1],land[i-1][3])
    land[i][3]+=max(land[i-1][0],land[i-1][1],land[i-1][2])

print(max(land[-1]))