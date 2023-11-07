# n개의 숫자로 구성된 숫자열 a_i와 m개의 숫자로 구성된 숫자열 b_j가 있다.
# 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.
tc=int(input())
for j in range(tc):
    n,m=map(int,input().split())
    array_n=list(map(int,input().split()))
    array_m=list(map(int,input().split()))
    res=[]
    if len(array_n)<len(array_m):
        s,l=len(array_n),len(array_m)
        short,long=array_n,array_m
    else:
        s,l=len(array_m),len(array_n)
        short,long=array_m,array_n
    for i in range(l-s+1):
        tmp=0
        for a,b in zip(short,long[i:s+i]):

            tmp+=a*b
        res.append(tmp)


    print(f"#{j+1} {max(res)}")