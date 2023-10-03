def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2

        else:
            n -= 1
            ans += 1
    return ans

# K 칸을 앞으로 점프하거나, (현재까지 온 거리) x 2에 해당하는 위치로 순간이동 가능
# K 칸을 점프하면 K 만큼의 건전지 사용량이 든다. 건전지 사용량 때문에 점프로 이동하는 것은 최소로 하려고 한다.
# 거꾸로 계산하며 접근해보기
n=6
ans=0 # 건전지 사용량
d=0 # 현재 거리

while n>0:
    if n%2==0:
        n//=2

    else:
        n-=1
        ans+=1
print(ans)