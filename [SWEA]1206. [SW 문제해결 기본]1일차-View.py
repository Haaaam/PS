for i in range(10):
    width=int(input())
    building=list(map(int,input().split()))
    cnt=0
    for j in range(2,width-2):
        next_max=max(building[j-1],building[j-2],building[j+1],building[j+2])
        if building[j]>next_max:
            cnt+=building[j]-next_max
    print(f"#{i+1} {cnt}")

