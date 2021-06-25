for i in range(int(input())):
    tmp=[]
    for j in range(int(input())):
        s,l=input().split()
        tmp.append([int(l),s])
    print(max(tmp)[1])



