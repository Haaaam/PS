n,k=map(int,input().split())
arr=list(map(int,input().split()))
tmp=[]
for i in range(1,len(arr)):
    tmp.append(arr[i]-arr[i-1])
tmp.sort()
print(sum(tmp[:n-k]))

