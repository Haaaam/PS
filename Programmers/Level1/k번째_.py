def solution(array,commands):
    answer = []
    for idx in range(len(commands)):
        i, j, k = commands[idx][0], commands[idx][1], commands[idx][2]
        tmp = array[i - 1:j]

        answer.append(sorted(tmp)[k - 1])

    return answer

array=[1,5,2,6,3,7,4]
commands=[[2,5,3],[4,4,1],[1,7,3]]
answer=[]
for idx in range(len(commands)):
    i,j,k=commands[idx][0],commands[idx][1],commands[idx][2]
    tmp=array[i-1:j]

    answer.append(sorted(tmp)[k-1])
print(answer)