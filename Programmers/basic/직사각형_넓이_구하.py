def solution(dots):
    dots = sorted(dots)
    row, col = 0, 0
    for i in range(1, len(dots)):
        if abs(dots[i - 1][0] - dots[i][0]) != 0:
            row = abs(dots[i - 1][0] - dots[i][0])
        if abs(dots[i - 1][1] - dots[i][1]) != 0:
            col = abs(dots[i - 1][1] - dots[i][1])
    return row*col
    # 다른 사람의 풀이!!!
    #return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])

dots=[[-1, -1], [1, 1], [1, -1], [-1, 1]]
dots=sorted(dots)
row,col=0,0
for i in range(1,len(dots)):
    if abs(dots[i-1][0]-dots[i][0])!=0:
        row=abs(dots[i-1][0]-dots[i][0])
    if abs(dots[i-1][1]-dots[i][1])!=0:
        col=abs(dots[i-1][1]-dots[i][1])
print(row*col)
