def solution(n):
    cnt=0
    while n != 1:
        cnt += 1
        if n % 2 == 0:
            n //= 2
        elif n % 2 != 0:
            n = (n * 3) + 1
        if cnt >= 500 and n != 1:
            cnt = -1
            break
    return cnt

n=16
cnt=0

while n!=1:
    cnt+=1
    if n%2==0:
        n//=2
    elif n%2!=0:
        n=(n*3)+1
    if cnt>=500 and n!=1:
        cnt=-1
        break
print(cnt)