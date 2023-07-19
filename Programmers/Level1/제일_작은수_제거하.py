def solution(arr):

    m=min(arr)
    arr.remove(m)
    if len(arr)!=0:
        return arr
    else:
        arr.append(-1)
        return arr

arr=[10]
print(solution(arr))