n,l=map(int,input().split())
location=sorted(list(map(int,input().split())))
s=location[0]
cnt=1

for i in range(1,n):
    if location[i]<s+l:
        pass
    else:
        cnt+=1
        s=location[i]

print(cnt)





