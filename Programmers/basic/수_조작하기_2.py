# "w":수에 1을 더한다.
# "s": 수에 1을 뺀다
# "d": 수에 10을 더한다.
# "a": 수에 10을 뺀다.
def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        a=numLog[i+1]
        if numLog[i]+1==a:
            answer+="w"
        elif numLog[i]-1==a:
            answer+="s"
        elif numLog[i]+10==a:
            answer+="d"
        else:
            answer+="a"

    return answer

numLog=[0,1,0,10,0,1,0,10,0,-1,-2,-1]
print(solution(numLog))