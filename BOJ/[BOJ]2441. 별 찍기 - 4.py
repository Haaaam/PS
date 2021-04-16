n=int(input())
for i in range(n,-1,-1):
    res="*"*(i)
    print(res.rjust(n))