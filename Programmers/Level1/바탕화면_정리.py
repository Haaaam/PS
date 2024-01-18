# 가장 왼쪽 위를 (0,0)으로 시작해 (세로 좌표, 가로 좌표)로 표현
# 빈칸은 ".", 파일이 있는 칸은 "#"의 값을 가진다.
# 드래그를하면 파일들을 선택할 수 있고, 선택된 파일들을 삭제할 수 있다.
# 최소한의 이동거리를 갖는 한 번의 드래그로 모든 파일을 선택해서 한 번에 지우려고 한다.
# return [lux,luy,rdx,rdy]
def solution(wallpaper):
    answer = [51, 51, 0, 0]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                answer[lux] = min(answer[lux], i)
                answer[luy] = min(answer[luy], j)
                answer[rdx] = max(answer[rdx], i + 1)
                answer[rdy] = max(answer[rdy], j + 1)
    return answer

wallpaper=[".#...","..#..","...#."]
lux,luy,rdx,rdy=0,1,2,3
answer=[51,51,0,0] # wallpaper의 범위를 넘지 않도록 초기설정
# left는 min으로 처리할 것이기때문에 최대 길이+1로 설정, right는 max로 처리할 것이기 때문에 최소길이-1로 설정
for i in range(len(wallpaper)):
    for j in range(len(wallpaper[i])):
        if wallpaper[i][j]=="#":
            answer[lux]=min(answer[lux],i)
            answer[luy]=min(answer[luy],j)
            answer[rdx]=max(answer[rdx],i+1)
            answer[rdy]=max(answer[rdy],j+1)

print(answer)

