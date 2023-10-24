n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    tmp=''
    if a<b:
        tmp="<"
    elif a==b:
        tmp="="
    elif a>b:
        tmp=">"
    print(f"#{i+1} {tmp}")