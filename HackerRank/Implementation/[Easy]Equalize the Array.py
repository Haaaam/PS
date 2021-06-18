def equalizeArray(arr):
    arr_cnt=[0]*(max(arr)+1)
    res=0
    for i in range(len(arr)):
        arr_cnt[arr[i]]+=1
    m=arr_cnt.index(max(arr_cnt))
    for i in arr:
        if i!=m:
            res+=1
    return res



n=int(input())
arr=list(map(int,input().split()))
print(equalizeArray(arr))