n=int(input())
ans=[]
res=[0]*n
for i in range(n):
    ans.append(list(map(int,input().split())))

for i in range(n):
    cnt=0
    for j in range(n):
        if i==j:
            continue
        elif ans[i][0]<ans[j][0] and ans[i][1]<ans[j][1]:
            cnt+=1
    res[i]=cnt+1
print(*res)

