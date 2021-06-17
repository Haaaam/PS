def stdDev(arr):
    global n
    m=sum(arr)/n
    res=0
    for i in arr:
        res+=(i-m)**2
    return (res/len(arr))**(1/2)
n=int(input())
arr=list(map(int,input().split()))
print(round(stdDev(arr),1))