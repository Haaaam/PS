import math
t=int(input())
for i in range(t):
    num=list(map(int,input().split()))
    print(f"#{i+1} {round(sum(num)/len(num))}")