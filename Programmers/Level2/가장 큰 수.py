numbers=list(map(int,input().split()))
num=[]
for i in numbers:
    if len(str(i))>1:
        num.append(int(j) for j in list(str(i)))
        print(i)
