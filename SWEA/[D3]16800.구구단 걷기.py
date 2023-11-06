import math
tc=int(input())
for i in range(tc):
    n=int(input())
    # i,j셀에는 정수 ixj 가 적혀 있다.
    # 즉, 당신이 (i,j)에 서 있다면, (i+1,j)나 (i,j+1)로 이동할 수 있다.
    # 정수 n이 주어질 때, n이 적혀 있는 어떤 셀에 도착하기 위해서 최소 몇번을 움직여야 하는가?


    arr=[]
    for idx in range(1,int(math.sqrt(n))+1):
        if n%idx==0:
            arr.append((idx,n//idx))

    for idx,(x,y) in enumerate(arr):
        arr[idx]=(x-1)+(y-1)
    print(f"#{i+1} {min(arr)}")