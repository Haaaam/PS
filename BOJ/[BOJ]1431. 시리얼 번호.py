res=[]

for i in range(int(input())):
    num=0
    n=input()
    for j in n:
        if j.isdigit():
            num+=int(j)
    res.append((n,num))
res.sort(key=lambda x:(len(x[0]),x[1],x[0]))

for i in res:
    print(i[0])
