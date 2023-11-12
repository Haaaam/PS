# n줄에는 nxn 행렬이 주어진다.
# n줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
tc=int(input())
for t in range(tc):
    n=int(input())
    array=[]
    for i in range(n):
        array.append(list(map(int,input().split())))
    res=[[0]*len(array) for _ in range(len(array))]

    # 90도, 180도, 270도 회전을 위한 array 초기화
    arr_90=[[0 for _ in range(n)] for _ in range(n)]
    arr_180=[[0 for _ in range(n)] for _ in range(n)]
    arr_270=[[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            arr_90[i][j]=array[n-j-1][i]

    for i in range(n):
        for j in range(n):
            arr_180[i][j]=arr_90[n-j-1][i]

    for i in range(n):
        for j in range(n):
            arr_270[i][j]=arr_180[n-j-1][i]

    print(f"#{t+1}")
    for i in range(n):
        for j in range(n):
            print(arr_90[i][j],end='')
        print(end=' ')
        for j in range(n):
            print(arr_180[i][j],end='')
        print(end=' ')
        for j in range(n):
            print(arr_270[i][j],end='')
        print()