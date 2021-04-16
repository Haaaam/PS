score=[]
ans=[]
res=0
for i in range(8):
    score.append(int(input()))
for i in range(5):
    res+=max(score)
    index=score.index(max(score))
    ans.append(index+1)
    score[index]=0
ans.sort()
print(res)
print(*ans)

