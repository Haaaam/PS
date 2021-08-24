# 시간 관리
n=int(input())
time=[]
for i in range(n):
    t,s=map(int,input().split())
    time.append(s-t)
time=sorted(time)
if time[0]<0:
    print(-1)
else:
    print(time[0])