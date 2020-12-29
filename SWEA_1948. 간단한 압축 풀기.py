for i in range(int(input())):
    n=int(input())
    res=''
    for _ in range(n):
        a=list(input().split())
        res+=a[0]*int(a[1])
    print('#{}'.format(i+1))

    for j in range(0,len(res),10):
        print(res[j:j+10])

