ans=[]
for i in range(9):
    ans.append(int(input()))
res=sum(ans)
for i in range(9):
    for j in range(9):
        if res-ans[i]-ans[j]==100:
            for k in range(9):
                if k==i or k==j:
                    continue
                else:
                    print(ans[k])
            exit()
