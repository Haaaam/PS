for i in range(int(input())):
    k=int(input())#층
    n=int(input())#호 수
    res=[j for j in range(1,n+1)]
    for x in range(k):
        for y in range(1,n):
            res[y]+=res[y-1]
    print(res[-1])

