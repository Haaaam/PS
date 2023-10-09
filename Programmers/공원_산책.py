def solution(park,routes):
    answer=[]
    re_x, re_y = 0, 0
    for idx in range(len(park)):
        for i in range(len(park[idx])):
            if park[idx][i] == "S":
                re_x, re_y = i, idx
                break

    for route in routes:

        op, n = route.split()
        n = int(n)
        x = re_x
        y = re_y
        for i in range(n):
            if op == "E" and x != len(park[0]) - 1 and park[y][x + 1] != 'X':
                x += 1
                if i == n - 1:
                    re_x = x
            elif op == "W" and x != 0 and park[y][x - 1] != 'X':
                x -= 1
                if i == n - 1:
                    re_x = x
            elif op == "S" and y != len(park) - 1 and park[y + 1][x] != 'X':
                y += 1
                if i == n - 1:
                    re_y = y
            elif op == "N" and y != 0 and park[y - 1][x] != 'X':
                y -= 1
                if i == n - 1:
                    re_y = y
    return [re_y,re_x]

park=["OSO","OXX","OOO"]
routes=	["E 2","S 3","W 1"]
re_x,re_y=0,0
for idx in range(len(park)):
    for i in range(len(park[idx])):
        if park[idx][i]=="S":
            re_x,re_y=i,idx
            break

for route in routes:

    op,n=route.split()
    n=int(n)
    x=re_x
    y=re_y
    for i in range(n):
        if op=="E" and x!=len(park[0])-1 and park[y][x+1]!='X':
            x+=1
            if i==n-1:
                re_x=x
        elif op=="W" and x!=0 and park[y][x-1]!='X':
            x-=1
            if i==n-1:
                re_x=x
        elif op=="S" and y!=len(park)-1 and park[y+1][x]!='X':
            y+=1
            if i==n-1:
                re_y=y
        elif op=="N" and y!=0 and park[y-1][x]!='X':
            y-=1
            if i==n-1:
                re_y=y
print([re_y,re_x])


