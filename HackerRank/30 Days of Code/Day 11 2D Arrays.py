arr=[list(map(int,input().split())) for _ in range(6)]
cnt=[]
for i in range(4):
    for j in range(4):
        s=0
        s+=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        cnt.append(s)
print(max(cnt))

