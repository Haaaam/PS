# 배열 조각하기
def solution(arr, query):
    for i in range(len(query)):

        a = query[i]
        if i % 2 == 0:

            arr = arr[:a + 1]

        else:
            arr = arr[a:]
    return arr

# 정수 배열 arr과 query가 주어진다
arr=[0,1,2,3,4,5]
query=[4,1,2]
for i in range(len(query)):

    a=query[i]
    if i%2==0:

        arr=arr[:a+1]

    else:
        arr=arr[a:]


print(arr)