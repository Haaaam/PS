#2021.05.08 resolving
n=int(input())
distance=list(map(int,input().split()))
price=list(map(int,input().split()))
cost=price[0]*distance[0]
target=price[0]
for i in range(1,n-1):
    if target>=price[i]:
        target=price[i]
    cost+=target*distance[i]
print(cost)
