arr_count=int(input())
arr=list(map(int,input().split()))
def migratoryBirds(arr):
    # Write your code here
    global arr_count
    tmp=[0]*(arr_count+1)
    for i in arr:
        tmp[i]+=1
    m=max(tmp)
    return tmp.index(m)

print(migratoryBirds(arr))



