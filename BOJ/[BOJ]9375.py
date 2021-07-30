def sol(n,wear,res):
    if n>0:
        for j in range(n):
            cloth,type=input().split()

            if type in wear:
                wear[type]+=1
            else:
                wear[type]=1

        for key,val in wear.items():
            res*=(val+1)

    return res-1
t=int(input())
for _ in range(t):
    n=int(input())
    wear=dict()
    res=1
    print(sol(n,wear,res))

