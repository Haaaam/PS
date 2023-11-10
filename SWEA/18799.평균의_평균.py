tc=int(input())
for t in range(tc):
    n=int(input())
    s=list(map(int,input().split()))

    a=sum(s)/len(s)

    print(f"#{t+1} {a}")
