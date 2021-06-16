def reverseArray(arr):
    tmp=[]
    for i in range(arr_count-1,-1,-1):
        tmp.append(arr[i])
    return tmp

arr_count=int(input())
arr=list(map(int,input().split()))
print(*reverseArray(arr))