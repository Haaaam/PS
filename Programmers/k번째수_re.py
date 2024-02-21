# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 한다.
# ex array가 [1,5,2,6,3,7,4], i=2,j=5,k=3이라면
# 1. array의 2번째부터 5번째까지 자르면 [5,2,6,3]
# 2. 1에서 나온 배열을 정렬하면 [2,3,5,6]
# 3. 2에서 나온 배열의 3번째 숫자는 5
# array [i,j,k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한
# 연산을 적용했을 때 나온 결과를 배열에 담아 return하도록 solution 함수를 작성
def solution(array,commands):
    answer=[]

    for t in range(len(commands)):
        i,j,k=commands[t][0],commands[t][1],commands[t][2]

        tmp=sorted(array[i-1:j])
        answer.append(tmp[k-1])

    return answer
array=[1,5,2,6,3,7,4]
commands=[[2,5,3],[4,4,1],[1,7,3]]
print(solution(array,commands))
