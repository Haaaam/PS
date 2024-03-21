# 각 칸마다 색이 칠해진 2차원 보드판이 있다.
# 그중 한 칸을 골랐을 때, 위, 아래, 왼쪽, 오른쪽 칸 중 같은 색깔로 칠해진 칸의 개수를 구하려고 한다.
# 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수를 return

# 정수를 저장할 변수 n을 만들고 board의 길이를 저장한다.
# 같은 색으로 색칠된 칸의 개수를 저장할 변수 count를 만들고 0을 저장한다.
# h와 w의 변화량을 저장할 정수 리스트 dh, dw를 만들고 각각 [0,1,-1,0],[1,0,0,-1]을 저장한다.
# 반복문을 이용해 i값을 0부터 3까지 1씩 증가시키며 아래 작업을 반복한다.
    # 체크할 칸의 h,w좌표를 나타내는 변수 h_check, w_check를 만들고 각각 h+dh[i], w+dw[i]를 저장한다.
    # nh가 0이상 n 미만이고 nw가 0이상 n 미만이라면 다음을 수행한다.
    # board[h][w]와 board[nh][nw]의 값이 동일하다면 count의 값을 1증가시킨다.
def solution(board, h, w):

    answer = 0 # 같은색으로 색칠된 칸의 개수
    n = len(board)
    dh, dw = [0,1,-1,0],[1,0,0,-1]

    for i in range(len(dh)):
        nh=h+dh[i]
        nw=w+dw[i]
        if 0<=nh<n and 0<=nw<n:
            if board[h][w]==board[nh][nw]:
                answer+=1

    return answer

board=[["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
h,w=1,1
print(solution(board,h,w))