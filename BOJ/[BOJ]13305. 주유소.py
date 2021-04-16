#2021.02.25
#[BOJ]13305. 주유소

n=int(input())
km=list(map(int,input().split()))
coin=list(map(int,input().split()))
cost=coin[0]*km[0]
target_coin=coin[0]
for i in range(1,n-1):
    if target_coin>=coin[i]:
        target_coin=coin[i]
    cost+=target_coin*km[i]
print(cost)

