#2021.02.24
#[BOJ]1292. 쉽게 푸는 문제

a,b=map(int,input().split())

num=[]
for i in range(1,b+1):
    for j in range(i):
        num.append(i)
        if len(num)>1001: break

print(sum(num[a-1:b]))


