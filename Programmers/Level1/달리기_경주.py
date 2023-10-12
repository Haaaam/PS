def solution(players,callings):
    for round in range(len(callings)):
        a = callings[round]  # 호명된 선수
        index = players.index(a)  # 호명된 선수의 현재 등수
        index_pre = players[index - 1]  # 호명된 선수의 앞에 있던 선수
        players[index - 1] = a
        players[index] = index_pre
    return players

# 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부른다.
# players: 1등부터 현재 등수 순서대로 담긴 문자열 배열
# callings: 해설진이 부른 이름을 담은 문자열 배열
players=["mumu","soe","poe","kai","mine"]
callings=["kai","kai","mine","mine"]

race=dict()
answer=[]
# 각 players의 순서를 dictionary 형태로 만들기
for i in range(len(players)):
    if players[i] not in race:
        race[players[i]]=i


for round in range(len(callings)):

    a = callings[round] # 호명된 선수
    index=race.get(a) # 앞지른 선수의 index

    index_pre=players[index-1] # 밀려난 선수

    # 앞지른 선수의 등수 -1
    race[a]-=1
    # 밀려난 선수의 등수 +1
    race[index_pre]+=1

    # players에서 위치 변경해주기
    players[index-1]=a

    players[index]=index_pre

print(players)

# 시간초과 남
"""
for round in range(len(callings)):
    a=callings[round] # 호명된 선수
    index=players.index(a) # 호명된 선수의 현재 등수
    index_pre=players[index-1] # 호명된 선수의 앞에 있던 선수
    players[index-1]=a
    players[index]=index_pre
"""




