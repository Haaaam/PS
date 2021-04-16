n=int(input())
for i in range(1,n+1):
    num=sum(1 for num in str(i) if num in ['3','6','9'])
    if num==0:
        print(i,end=' ')
    else:
        print("-"*num,end=' ')
