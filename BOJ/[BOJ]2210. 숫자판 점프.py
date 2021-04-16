array=[]
ans=[]
for i in range(5):
    array.append(list(map(str,input().split())))

#이동할 네 방향(상,하,좌,우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y,n):
    if len(n)<6:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
        #범위 내에 있을경우
            if 0<=nx<5 and 0<=ny<5:
                dfs(nx,ny,n+array[nx][ny])
        # 길이가 6이 될경우
    else:
        if n not in ans:
            ans.append(n)
        return

for i in range(5):
    for j in range(5):
        dfs(i,j,array[i][j])
print(len(ans))


