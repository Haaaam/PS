
def solution(n,t):
    for i in range(1, t + 1):
        n *= 2
    return n

n,t=7,15

for i in range(1,t+1):
    n*=2

print(n)

