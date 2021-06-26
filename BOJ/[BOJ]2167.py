import sys
input=sys.stdin.readline
def sol(i,j,x,y):
    sum=0
    for a in range(i-1,x):
        for b in range(j-1,y):
            sum+=array[a][b]
    return sum
n,m=map(int,input().split())
array=[]
for _ in range(n):
    array.append(list(map(int,input().split())))
k=int(input())
for _ in range(k):
    i,j,x,y=map(int,input().split())
    print(sol(i,j,x,y))