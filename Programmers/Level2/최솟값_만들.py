def solution(A,B):
    answer = 0
    A=sorted(A)
    B=sorted(B,reverse=True)
    for i in range(len(A)):
        answer+=A[i]*B[i]

    return answer

A=[1,4,2]
B=[5,4,4]
B=sorted(B,reverse=True)
answer=0
for i in range(len(A)):
    answer+=A[i]*B[i]
print(answer)