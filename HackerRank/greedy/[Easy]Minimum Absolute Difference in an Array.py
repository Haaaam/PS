def minimumAbsoluteDifference(arr):
    ans=[]
    arr.sort()
    for i in range(1,len(arr)):
        ans.append(abs(arr[i]-arr[i-1]))
    return min(ans)

n=int(input())
arr=list(map(int,input().split()))

print(minimumAbsoluteDifference(arr))