#2021.03.02
#[BOJ]9663. N-Queen

n=int(input())
row=[0]*n
res=0

def check(x):
    for i in range(x):
        if row[x]==row[i]:
            return False
        if abs(row[x]-row[i])==x-i:
            return False
    return True

def dfs(x):
    global res
    if x==n:
        res+=1
    else:
        for i in range(n):
            row[x]=i
            if check(x):
                dfs(x+1)

dfs(0)
print(res)

