import math
tc=int(input())
for t in range(tc):
    a,b=map(int,input().split())
    cnt=0
    for i in range(a,b+1):
        tmp=math.sqrt(i)
        if tmp==int(tmp):
            i=str(i)
            tmp=str(int(tmp))
            # 뒤집어도 동일한 수면 제곱 팰린드롬 수
            if i==i[::-1] and tmp==tmp[::-1]:
                cnt+=1
    print(f"#{t+1} {cnt}")