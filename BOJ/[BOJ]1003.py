def sol(n):
    global z,o
    for i in range(n+1):
        if i==0:
            z[0]=1
        elif i==1:
            o[1]=1
        else:
            z[i]=z[i-2]+z[i-1]
            o[i]=o[i-2]+o[i-1]
    return z[i],o[i]
t=int(input())
for _ in range(t):
    n=int(input())
    z = [0] * (n + 1)
    o = [0] * (n + 1)
    print(*sol(n))

