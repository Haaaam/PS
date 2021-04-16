arr=list(map(int,input().split()))
ans=[1,2,3,4,5]
while True:
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            arr[i-1],arr[i]=arr[i],arr[i-1]
            print(*arr)
    if arr==ans:
        break





