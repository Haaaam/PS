dx=[0,1,0,-1] # 우,하,좌,상
dy=[1,0,-1,0]

tc=int(input())

for t in range(tc):
    n=int(input())
    r,c=0,0
    array=[[0]*n for _ in range(n)]
    dist=0
    for i in range(1,n*n+1):
        array[r][c]=i
        r+=dx[dist]
        c+=dy[dist]
        # 배열의 범위를 벗어나지 않는 범위 내에서만 수행
        if r<0 or c<0 or r>=n or c>=n or array[r][c]!=0:
            r-=dx[dist]
            c-=dy[dist]
            dist=(dist+1)%4

            r+=dx[dist]
            c+=dy[dist]

    print(f"#{t+1}")
    for j in array:
        print(*j)
