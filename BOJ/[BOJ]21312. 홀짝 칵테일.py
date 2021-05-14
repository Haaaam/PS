arr=list(map(int,input().split()))
res=1
check=False
for i in range(len(arr)):
    if arr[i]%2!=0:
        res*=arr[i]
        check=True
if check:
    print(res)
else:
    for i in arr:
        res*=i
    print(res)