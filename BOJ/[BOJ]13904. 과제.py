#2021.03.09
#[BOJ]13904. 과제

n=int(input())
date=sorted([list(map(int,input().split())) for i in range(n)],key=lambda x:(-x[1],x[0]))
lastday=max(date)[0]
visited=[False]*n
res=0
for day in range(lastday,0,-1):
    for j in range(len(date)):
        if visited[j]==False and date[j][0]>=day:
            visited[j]=True
            res+=date[j][1]
            break
print(res)



