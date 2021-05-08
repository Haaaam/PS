n=int(input())
tips=[int(input()) for _ in range(n)]
tips.sort(reverse=True)
cost=0
for i in range(len(tips)):
    result=tips[i]-(i+1-1)
    if result<0:
        result=0
    cost+=result
print(cost)
