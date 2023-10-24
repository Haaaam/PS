n=int(input())
for i in range(n):
    num=list(map(int,input().split()))
    print(f"#{i+1} {sum(i for i in num if i%2!=0)}")