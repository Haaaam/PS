for i in range(int(input())):
    num=int(input())
    test=list(map(int,input().split()))
    dp=[0]*101
    for j in test:
        dp[j]+=1
    res=max(dp)
    for k in range(100,-1,-1):
        if res==dp[k]:
             print("#%d %d"%(i+1,k))
