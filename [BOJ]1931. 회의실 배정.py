n=int(input())
time=sorted([list(map(int,input().split()))
             for i in range(n)],key=lambda x:(x[1],x[0]))
end=0
res=0

for i in time:
    if i[0]>=end:
        end=i[1]
        res+=1
print(res)

