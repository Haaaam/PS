# 시간 관리(다시풀기)
n=int(input())
time=[list(map(int,input().split())) for _ in range(n)]
time.sort(key=lambda x:x[1],reverse=True)
s=time[0][1]-time[0][0]
for i in range(1,n):
    if s>time[i][1]:
        s=time[i][1]-time[i][0]
    else:
        s-=time[i][0]
if s<0:
    print(-1)
else:
    print(s)