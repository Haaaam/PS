#def solution(arr1,arr2):
#    answer=[]
#    for i in range(len(arr1)):
#        tmp=[]
#        for j in range(len(arr1[i])):
#            tmp.append(arr1[i][j]+arr2[i][j])

#        answer.append(tmp)

#    return answer

def solution(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j]+=arr2[i][j]
    return arr1
print(solution([[1,2],[2,3]],[[3,4],[5,6]]))