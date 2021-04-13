import sys
input=sys.stdin.readline

def find_parent(x):
    if x==parent[x]:
        return x
    return find_parent(parent[x])

def union_parent(x,y):
    x=find_parent(x)
    y=find_parent(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

n,m=map(int,input().split())

parent=[i for i in range(n)]
node=[ tuple(map(int,input().split())) for _ in range(m)]

for i,j in enumerate(node):
    if find_parent(j[0])!=find_parent(j[1]):
        union_parent(j[0],j[1])
    else:
        print(i+1)
        break
else:
    print(0)