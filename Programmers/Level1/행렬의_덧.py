def solution(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j]+=arr2[i][j]

    return arr1

arr1=[[1],[2]]
arr2=[[3],[4]]
res=0
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        arr1[i][j]+=arr2[i][j]
print(arr1)

