# 컴퓨터 바탕화면은 각 칸이 정사각형인 격자판
# wallpaper: 컴퓨터 바탕화면의 상태를 나타낸 문자 배열
# 파일들은 바탕화면의 격자칸에 위치하고 바탕화면의 격자점들은 바탕화면의 가장 왼쪽 위를 (0,0)
# 으로 시작해 (세로 좌표, 가로 좌표)로 표현한다. 빈칸은 ".", 파일이 있는 칸은 "#"의 값을 가진다
# 드래그를 하면 파일들을 선택할 수 있고, 선택된 파일들을 삭제할 수 있다.
# S(lux,luy) -> E(rdx,rdy) ; 시작점 -> 끝점
# 드래그 한 거리: |rdx-lux| +|rdy-luy|로 정의
# 최소한의 이동거리를 갖는 드래그의 시작점과 끝점 찾기
# return [lux,luy,rdx,rdy]
def solution(wallpaper):
    # 1<= wallpaper length <=50, 1<=wallpaper[i] length <=50
    # left는 min으로 처리, right는 max로 처리할 것이기때문에 초기값을 다음과 같이 설정
    direction=[51,51,0,0] # wallpaper의 최대 길이
    lux,luy,rdx,rdy=0,1,2,3
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j]=="#":
                direction[lux]=min(direction[lux],i)
                direction[luy]=min(direction[luy],j)
                direction[rdx]=max(direction[rdx],i+1)
                direction[rdy]=max(direction[rdy],j+1)

    return direction

wallpaper=["..........", ".....#....", "......##..", "...##.....", "....#....."]
print(solution(wallpaper))