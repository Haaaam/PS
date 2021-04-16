n,m=map(int,input().split())
cnt=0
a=[list(map(int,list(input()))) for _ in range(n)]
b=[list(map(int,list(input()))) for _ in range(n)]

#3x3의 부분 행렬에 있는 모든 원소를 바꿔주기 위함
def reverse(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            a[i][j]=1-a[i][j]
#두 행렬이 같은지 비교
def checkArray():
    for i in range(n):
        for j in range(m):
            if a[i][j]!=b[i][j]:
                return 0
    return 1

#행렬을 초과하지 않게 -2를 해준다.
for i in range(n-2):
    for j in range(m-2):
        if a[i][j]!=b[i][j]:
            reverse(i,j)
            cnt+=1

#a를 b로 바꾸는데 필요한 연산의 횟수의 최솟값 출력
if checkArray():
    print(cnt)
#a를 b로 바꿀 수 없는 경우 -1출력
else:
    print(-1)