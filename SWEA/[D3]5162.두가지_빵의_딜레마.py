# 은비는 두 가지 맛의 빵 밖에 먹지 않는다.
# 하나는 현미 빵: A원
# 단호박 빵: B원
# 현재 은비는 C원을 가지고 있으며, 어떤 빵이든 상관없이 그냥 많은 개수의 빵을 사고 싶다.
# 두 종류의 개수를 다르게 혹은 한종류의 빵만 사도 된다. 최대 몇 개의 빵을 살 수 있을까?
tc=int(input())
for i in range(1,tc+1):
    a,b,c=map(int,input().split())
    res=0
    if a<b:
        res+=(c//a)
    else:
        res+=(c//b)
    print(f"#{i} {res}")