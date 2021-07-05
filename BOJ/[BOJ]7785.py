#[String]회사에 있는 사람
import sys
input=sys.stdin.readline

n=int(input())
ans=[]
for i in range(n):
    a=list(input().split())
    if a[1]=='enter':
        ans.append(a[0])
    elif a[1]=='leave':
        ans.remove(a[0])
for i in sorted(ans,reverse=True):
    print(i)