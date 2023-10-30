import math
n=int(input())
for i in range(n):
    n,d=map(int,input().split()) # n: 심겨진 꽃의 갯수
    #좌표 x에 분무기를 놓았을 경우 닫힌 구간[x-D,x+D]에 심긴 모든 꽃들에 물을 줄 수 있다.

    # 한 분무기로 물을 줄 수 있는 꽃의 갯수
    d=d*2+1

    res=n//d
    if n%d!=0:
        res+=1

    print(f"#{i+1} {res}")
