def sol(n,grid):
    for i in range(1,(n-2)+1):
        for j in range(1,(n-2)+1):
            if grid[i][j]>max(grid[i-1][j],grid[i][j-1],grid[i][j+1],grid[i+1][j]):
                grid[i][j]='X'
    return grid
n=int(input())
grid=[list(str(input())) for i in range(n)]

for i in range(1,(n-2)+1):
    for j in range(1,(n-2)+1):
        if grid[i][j]>max(grid[i-1][j],grid[i][j-1],grid[i][j+1],grid[i+1][j]):
            grid[i][j]='X'
for i in range(n):
    print(''.join(sol(n,grid)[i]))

