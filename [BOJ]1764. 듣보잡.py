import sys
input=sys.stdin.readline
n,m=map(int,input().split())
ln=[]
res=[]
for _ in range(n+m):
    ln.append(input())
ln.sort()
i=0
while i<n+m-1:
   if ln[i]==ln[i+1]:
       res.append(ln[i])
       i+=2
   else:
       i+=1

print(len(res))
for i in res:
    print(i)