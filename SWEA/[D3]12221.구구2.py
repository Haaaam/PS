n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    res=a*b
    if a>=10 or b>=10:
        res=-1

    print(f"#{i+1} {res}")