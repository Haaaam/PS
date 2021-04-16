n,m=map(int,input().split())
card=list(map(int,input().split()))
res=0
for i in range(len(card)):
    for j in range(i+1,len(card)):
        for k in range(j+1,len(card)):
            value=card[i]+card[j]+card[k]
            if value<=m:
                res=max(value,res)

print(res)