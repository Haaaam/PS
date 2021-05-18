tot=[[0,0,0,1],[0,0,0,2],[0,0,0,3]]
for i in range(int(input())):
    score=list(map(int,input().split()))
    for j in range(len(score)):
        tot[j][0] += score[j]
        if score[j]==3:tot[j][1]+=1
        elif score[j]==2:tot[j][2]+=1
tot.sort(reverse=True)

res=0

if tot[0][0]!=tot[1][0]:
    res=tot[0]

elif tot[0][0]==tot[1][0]:
    if tot[0][1]>tot[1][1]:
        res=tot[0]

    else:
        if tot[0][2]>tot[1][2]:
            res=tot[0]
        elif tot[0][2]==tot[1][2]:
            res=[tot[0][0],0,0,0]

elif tot[0][0]==tot[1][0]and tot[1][0]==tot[2][0]:
    if tot[0][1]>tot[1][1]:
        res=tot[0]
    elif tot[0][1]==tot[1][1]:
        if tot[0][2]>tot[1][2]:
            res=tot[0]
        else:
            res=[tot[0][0],0,0,0]
print(res[-1],res[0])








