#2021.02.14
#[BOJ]10825. 국여수

n=int(input())
score=[]
for i in range(n):
    score.append(input().split())
score.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in score:
    print(i[0])

