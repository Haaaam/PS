n=int(input())
graph=[-1]*(n+1)
cnt=0
for i in range(1,n+1):
    cow,location=map(int,input().split())
    if graph[cow]==-1:
        graph[cow]=location
    elif graph[cow]!=location:
        cnt+=1
        graph[cow]=location
print(cnt)