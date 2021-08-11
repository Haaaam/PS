n=int(input())
num=sorted(list(map(int,input().split())))
if n%2==0:
    print(num[n//2-1])
else:
    print(num[n//2])


