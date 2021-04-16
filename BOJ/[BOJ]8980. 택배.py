n,c=map(int,input().split())
m=int(input())
graph=sorted([list(map(int,input().split())) for _ in range(m)],key=lambda x:(x[1]))

cnt=0
box=[c]*(n+1)

for i in range(m):
    temp=c
    for j in range(graph[i][0],graph[i][1]):
        temp=min(temp,box[j])
    temp=min(temp,graph[i][2])
    for j in range(graph[i][0],graph[i][1]):
        box[j]-=temp
    cnt+=temp
print(cnt)


