for i in range(int(input())):
    n,m=map(int,input().split())
    res=""
    if m==0:
        print('#{} {}'.format(i+1,"OFF"))
    else:
        while m>0:
            res=str(m%2)+res
            m//=2
        if res[-n:]!="1"*n:
            print('#{} {}'.format(i+1,'OFF'))
        else:
            print('#{} {}'.format(i+1,'ON'))

