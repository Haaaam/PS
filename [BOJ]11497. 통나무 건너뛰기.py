#2021.02.22
#[BOJ]1496. 통나무 건너뛰기

t=int(input())
for i in range(t):
    n=int(input())
    tree=list(map(int,input().split()))
    tree.sort()
    res=0
    for j in range(2,n):
        res=max(res,abs(tree[j]-tree[j-2]))
    print(res)

