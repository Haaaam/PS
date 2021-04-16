import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=sorted([int(input()) for _ in range(n)])
b={}
for i,j in enumerate(a):
    if j not in b.keys():
        b[j]=i
for _ in range(m):
    d=int(input())
    print(-1 if d not in b.keys() else b[d])

    
'''def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None
n,m=map(int,input().split())
a=sorted([int(input()) for _ in range(n)])

for i in range(m):
    d=int(input())
    index=binary_search(a,d,0,m-1)
    if index!=None:
        print(index)
    else:
        print(-1)'''


