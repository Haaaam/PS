#2021.02.12
#[BOJ]1236. 성지키기

n,m=map(int,input().split())
graph=[list(input()) for _ in range(n)]
row=[0]*n
col=[0]*m
for i in range(n):
    for j in range(m):
        if graph[i][j]=='X':
            row[i]=1
            col[j]=1
row_cnt=0
col_cnt=0
for i in range(n):
    if row[i]==0:
        row_cnt+=1
for i in range(m):
    if col[i]==0:
        col_cnt+=1
print(max(row_cnt,col_cnt))


