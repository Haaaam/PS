def closestNumbers(arr):
    arr=sorted(arr)
    tmp=[]
    for i in range(1, len(arr)):
        tmp.append([abs(arr[i] - arr[i - 1]), arr[i], arr[i - 1]])
    tmp=sorted(tmp)
    res=[tmp[0][1],tmp[0][2]]
    for i in range(1,len(tmp)):
        if tmp[i][0]==tmp[i-1][0]:
            res.append(tmp[i][1])
            res.append(tmp[i][2])
        else:
            break

    return sorted(res)
n=int(input())
arr=list(map(int,input().split()))
print(*closestNumbers(arr))
