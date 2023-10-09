def solution(park, routes):

    re_x, re_y = 0, 0
    # 시작 위치 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                re_y, re_x = i, j
                break

    y, x = re_y, re_x

    for route in routes:

        op, n = route.split(' ')
        n = int(n)
        for step in range(n):
            #
            if op == "E" and x != len(park[0]) - 1 and park[y][x + 1] != 'X':
                x += 1
                if step == n - 1:
                    re_x = x

            elif op == "W" and x != 0 and park[y][x - 1] != 'X':
                x -= 1
                if step == n - 1:
                    re_x = x

            elif op == "S" and y != len(park) - 1 and park[y + 1][x] != 'X':
                y += 1
                if step == n - 1:
                    re_y = y
            elif op == "N" and y != 0 and park[y - 1][x] != 'X':
                y -= 1
                if step == n - 1:
                    re_y = y
    return [re_y,re_x]
# [방향 거리, 방향 거리, ....]
# 주어진 방향으로 이동할 때 공원을 벗어나는지 확인
# 주어진 방향으로 이동 중 장애물을 만나는지 확인
# 공원의 가로 길이가 W, 세로 길이가 H
# 공원의 좌측 상단 좌표는 (0,0), ..... (H-1, W-1)
# park: 공원을 나타내는 문자열 배열
# routes: 로봇 강아지가 수행할 명령이 담긴 문자열 배열
# return 모든 명령 수행 후 놓인 위치[세로 방향 좌표, 가로 방향 좌표]

park=["OSO","OOO","OXO","OOO"]
routes=["E 2","S 3","W 1"]
answer=[]
re_x,re_y=0,0
# 시작 위치 찾기
for i in range(len(park)):
    for j in range(len(park[i])):
        if park[i][j]=="S":
            re_y,re_x=i,j
            break

for route in routes:
    y,x=re_y,re_x
    op,n=route.split(' ')
    n=int(n)
    for step in range(n):
        #
        if op=="E" and x!=len(park[0])-1 and park[y][x+1]!='X':
            x+=1
            if step==n-1:
                re_x=x

        elif op=="W" and x!=0 and park[y][x-1]!='X':
            x-=1
            if step==n-1:
                re_x=x

        elif op=="S" and y!=len(park)-1 and park[y+1][x]!='X':
            y+=1
            if step==n-1:
                re_y=y
        elif op=="N" and y!=0 and park[y-1][x]!='X':
            y-=1
            if step==n-1:
                re_y=y
        print(re_y,re_x)
print(re_y,re_x)




