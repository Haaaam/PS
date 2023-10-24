t=int(input())
for i in range(t):
    n=int(input())

    if n%2==0:
        tmp="Even"
    else:
        tmp="Odd"
    print(f"#{i+1} {tmp}")
