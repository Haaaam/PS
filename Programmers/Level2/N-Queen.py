# 한 행에 하나의 퀸만 있다고 생각하고 풀기

def dfs(queen,n,x):
    res=0
    if x==n:
        res=1

    else:
        for i in range(n):

            queen[x]=i

            # 세로 제거
            for j in range(x):
                if queen[x]==queen[j]:
                    break

                # 대각선일 제거
                if abs(queen[x]-queen[j])==x-j:
                    break

            else:
                res+=dfs(queen,n,x+1)

    return res




def solution(n):
    queen=[0]*n


    return dfs(queen,n,0)


n=int(input())


# 퀸 n개를 서로 공격할 수 없게 놓는 경우의 수를 출력
print(solution(n))