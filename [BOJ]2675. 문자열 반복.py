for i in range(int(input())):
    r,s=input().split()
    r=int(r)
    p=[]
    for k in s:
        p.append(k*r)
    for j in p:
        print(j,end='')
    print()