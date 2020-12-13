n,m,k=map(int,input().split())
seat=0
for i in range(n):
    for j in range(m):
        seat+=1
        if k==seat-1:
            print(i,j,end=' ')