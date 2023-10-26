def move(x,y,direction):
    before_x=x
    before_y=y

    if direction=="U":
        if y<5:
            y+=1
    elif direction=="D":
        if -5<y:
            y-=1
    elif direction=="R":
        if x<5:
            x+=1
    elif direction=="L":
        if x>-5:
            x-=1

    return before_x,before_y,x,y


def solution(dirs):
    answer=0
    check={}
    x,y=0,0

    for direction in dirs:

        before_x,before_y,x,y=move(x,y,direction)
        if before_x!=x or before_y!=y:
            # 처음 가본 길만 추가해야 하므로 (0,0)->(0,1)을 지났다면 (0,1)->(0,0) 이렇게도 지나간 것으로 본다.
            key1=f"{before_x}, {before_y}, {x}, {y}"
            key2=f"{x}, {y}, {before_x}, {before_y}"
            if key1 in check or key2 in check:
                continue
            else:
                check[key1]=True
                check[key2]=True
                answer+=1

    return answer


dirs="LULLLLLLU"
dirs=list(dirs)
print(solution(dirs))


