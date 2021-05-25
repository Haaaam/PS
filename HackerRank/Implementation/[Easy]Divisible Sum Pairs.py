def divisibleSumPairs(n,k,ar):
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k==0:
                cnt+=1
    return cnt

n,k=map(int,input().split())
ar=list(map(int,input().split()))
result=divisibleSumPairs(n,k,ar)
print(result)

