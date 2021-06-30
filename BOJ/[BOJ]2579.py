#계단 오르기
'''
[규칙]
1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
3. 마지막 도착 계단은 반드시 밟아야 한다.
'''

n=int(input())
stairs=[int(input()) for _ in range(n)]
def sol(stairs,n):
    d=[0]*n
    for i in range(n):
        if i==0:
            d[0]=stairs[0]
            continue
        elif i==1:
            d[1]=max(stairs[i]+d[i-1],stairs[i])
            continue
        elif i==2:
            d[2]=max(stairs[i]+d[i-2],stairs[i]+stairs[i-1])
            continue
        d[i]=max(stairs[i]+stairs[i-1]+d[i-3],stairs[i]+d[i-2])
    return d[-1]

print(sol(stairs,n))
