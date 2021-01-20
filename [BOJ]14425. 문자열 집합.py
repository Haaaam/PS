n,m=map(int,input().split())
s=[]
cnt=0
for i in range(n):
    s.append(input())
for i in range(m):
    l=input()
    if l in s:
        cnt+=1
    else:
        continue
print(cnt)

