# 8x8 체스보드에 8개의 퀸을 서로 공격하지 못하게 놓는 문제
# 퀸은 같은 행, 열, 또는 대각선 위에 있는 말을 공격할 수 있따.
# nxn 보드에 n개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는 몇가지가 있을까?
# 퀸을 놓는 방법의 수 return

def check(x):

    for i in range(x):
        if row[x]==row[i]:
            return False
        if abs(row[x]-row[i])==x-i:
            return False

    return True

def dfs(x):
    global res
    global row
    if x==n:
        res+=1
    else:
        for i in range(n):

            row[x]=i
            if check(x):
                dfs(x+1)

tc=int(input())
for t in range(tc):
    n=int(input())
    row=[0]*n
    res=0
    dfs(0)

    # 퀸 n개를 서로 공격할 수 없게 놓는 경우의 수를 출력
    print(f"#{t+1} {res}")
