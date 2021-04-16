n=int(input())
k=int(input())
arr=sorted(list(map(int,input().split())))
if k>n:
    print(0)
else:
    distance=[]
    for i in range(len(arr)-1):
        distance.append(arr[i+1]-arr[i])

    for i in range(k-1):
        m=max(distance)
        distance.remove(m)
    print(sum(distance))

