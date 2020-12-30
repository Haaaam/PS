for i in range(int(input())):
    n=int(input())
    res=0
    for j in range(n):
        t=input().split()
        p=float(t[0])
        x=int(t[1])
        res+=p*x
    print("#%d %.6f"%(i+1,res))


    