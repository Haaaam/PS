# n^2 배열 자르기
"""
def solution(n,left,right):
    arr_new=[]
    arr=[[i+1]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i>j:
                arr[i][j]=i+1
            elif i<j:
                arr[i][j]=j+1
            arr_new.append(arr[i][j])
    return arr_new[left:right+1]
"""

def solution(n,left,right):
    arr=[]
    for i in range(left,right+1):
        a=max(i//n,i%n)
        arr.append(a+1)
    return arr
n,left,right=3,2,5
print(solution(n,left,right))