for i in range(int(input())):
    n=int(input())
    res=[]
    for j in range(n):
        res.append('1/%d'%n)
    print(f'#{i+1} {" ".join(res)}')