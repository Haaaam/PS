# 머쓱이는 RPG 게임을 하고 있다. 게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위,아래,
# 왼쪽, 오른쪽으로 한 칸씩 이동한다.
# [0,0]에서 up:[0,1]
# down:[0,-1]
# left: [-1,0]
# right: [1,0]

def solution(keyinput,board):
    answer = [0, 0]
    if board[0]==0 and board[1]==0:
        return answer
    for direct in keyinput:
        if direct == "left":
            answer[0] -= 1
            if abs(answer[0])>board[0]//2:
                answer[0]+=1
        elif direct == "right":
            answer[0] += 1
            if answer[0]>board[0]//2:
                answer[0]-=1
        elif direct == "up":
            answer[1] += 1
            if answer[1]>board[1]//2:
                answer[1]-=1

        elif direct == "down":
            answer[1] -= 1
            if abs(answer[1])>board[1]//2:
                answer[1]+=1


    return answer

keyinput=["left", "left", "left", "right"]
board=[3,3]

print(solution(keyinput,board))

