def solution(M,N):
    if M>=N:
        return (M-1)+(N-1)*2
    else:
        return (N-1)+(M-1)*2
M,N=1,1
print(solution(M,N))

