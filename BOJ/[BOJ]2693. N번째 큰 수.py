for i in range(int(input())):
    A=list(map(int,input().split()))
    A.sort(reverse=True)
    print(A[2])
