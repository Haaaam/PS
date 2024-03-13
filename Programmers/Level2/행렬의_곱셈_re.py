# 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수


def solution(arr1, arr2):
    answer = []
    r1,c1=len(arr1),len(arr1[0])
    r2,c2=len(arr2),len(arr2[0])
    for r in range(r1):
        line=[]
        for i in range(c2):
            tmp=0
            for j in range(c1):
                tmp+=(arr1[r][j]*arr2[j][i])
            line.append(tmp)
        answer.append(line)

    return answer

arr1=[[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2=[[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1,arr2))
