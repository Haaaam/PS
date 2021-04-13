# 승원이가 도킹시킬 수 있는 최대의 비행기 수를 출력
import sys
input=sys.stdin.readline

def find_parent(x):
    if x==parent[x]:
        return x
    par=find_parent(parent[x])
    parent[x]=par

    return parent[x]

def union_parent(x,y):
    x=find_parent(x)
    y=find_parent(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

g=int(input())
cnt=0
airplanes=[int(input()) for _ in range(int(input()))]
parent={i:i for i in range(g+1)}

for airplane in airplanes:
    x=find_parent(airplane)
    if x==0:
        break
    union_parent(x,x-1)
    cnt+=1
print(cnt)




