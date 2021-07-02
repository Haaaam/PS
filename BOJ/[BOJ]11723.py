#집합
import sys
input=sys.stdin.readline
m=int(input())
s=[]
for i in range(m):
    a=list(input().split())
    if a[0]=='add':
        if int(a[1]) not in s:
            s.append(int(a[1]))
    elif a[0]=='check':
        if int(a[1]) in s:
            print(1)
        else:
            print(0)
    elif a[0]=='remove':
        if int(a[1]) in s:
            s.remove(int(a[1]))
    elif a[0]=='toggle':
        if int(a[1]) in s:
            s.remove(int(a[1]))
        else:
            s.append(int(a[1]))
    elif a[0]=='all':
        s=[i for i in range(1,21)]
    else:
        s=[]


