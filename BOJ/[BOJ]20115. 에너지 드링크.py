n=int(input())
drinks=sorted(list(map(int,input().split())),reverse=True)
res=drinks[0]
for i in range(1,n):
    res+=drinks[i]/2
print(res)

