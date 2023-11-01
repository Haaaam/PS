# 준환이는 이번 주에 x분만큼 운동 하였다
# 준환이가 제한되어 있는 시간을 넘은 운동을 한 것인지, 그것이 아니라면 몇 분 더 운동을 해야 제한을 맞출 수 있는지 출력
# 1주일에 l분이상 u분이하의 운동, 준환이는 x분만큼 운동
tc=int(input())
for i in range(tc):
    l,u,x=map(int,input().split())
    res=0
    if x<l:
        res=l-x
    elif x>=l and x<=u:
        res=0
    elif x>u:
        res=-1
    print(f"#{i+1} {res}")