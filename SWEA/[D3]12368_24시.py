n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a+b<24:
        print(f"#{i+1} {a+b}")
    elif a+b==24:
        print(f"#{i+1} {0}")
    else:
        print(f"#{i+1} {(a+b)-24}")