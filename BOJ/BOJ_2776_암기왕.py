def binary_search(array,target,start,end):
    while start<=end:
        mid=(end+start)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    m=int(input())
    b=list(map(int,input().split()))
    for j in b:
        result=binary_search(a,j,0,n-1)
        if result!=None:
            print(1)
        else:
            print(0)
