import sys
input=sys.stdin.readline

def find_parent(x):
    if x==parent[x]:
        return x

    parent[x]=find_parent(parent[x])
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
parent=[i for i in range(g+1)]

for airplane in airplanes:
    gate=find_parent(airplane)
    if gate==0:
        break
    union_parent(gate,gate-1)

    cnt+=1
print(cnt)







