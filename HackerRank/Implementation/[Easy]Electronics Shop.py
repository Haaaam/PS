def getMoneySpent(keyboards,drives,n):
    ans=[]
    for i in keyboards:
        for j in drives:
            if i+j<=n:
                ans.append(i+j)
    if ans:
        return max(ans)
    else:
        return -1

n,m,b=map(int,input().split())
keyboards=list(map(int,input().split()))
drives=list(map(int,input().split()))
print(getMoneySpent(keyboards,drives,n))