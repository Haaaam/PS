def sol(n,c):
    cnt=0
    for i in range(n):
        if i<n-2 and c[i+2]==1:
            i+=1

        cnt+=1
    return cnt
n=int(input())
c=list(map(int,input().split()))

print(sol(n,c))