tc=int(input())
for t in range(tc):
    n=int(input())
    res=-1

    for i in range(1,n+1):
        # i의 세제곱근이 n보다 커지면 종료
        if i**3>n:
            break
        if n==i**3:
            res=i
            break


    print(f"#{t+1} {res}")