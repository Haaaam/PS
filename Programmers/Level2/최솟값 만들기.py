A=list(map(int,input().split()))
B=list(map(int,input().split()))

def solution(A,B):
    A=sorted(A)
    B=sorted(B,reverse=True)
    answer=0
    for i in range(len(A)):
        answer+=(A[i]*B[i])
    return answer
print(solution(A,B))