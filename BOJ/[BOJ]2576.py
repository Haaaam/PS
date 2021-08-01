#홀수
ans=[]
for i in range(7):
    n=int(input())
    if n%2!=0:
        ans.append(n)
if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)

