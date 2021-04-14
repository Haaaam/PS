n,m=map(int,input().split())
j=int(input()) #사과의 개수

s,e=1,m
ans=0

for i in range(j):
    apple=int(input())

    if apple<s:
        ans+=(s-apple)
        s=apple
        e=apple+m-1
    elif apple>e:
        ans+=(apple-e)
        e=apple
        s=e-m+1


print(ans)