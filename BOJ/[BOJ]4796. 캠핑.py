i=1
while True:
    L,P,V=map(int,input().split())
    res=0
    if L==0 and P==0 and V==0:
        break
    res+=L*(V//P)+min(V%P,L)
    print(f'Case {i}: {res}')
    i+=1


