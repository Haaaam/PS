
for _ in range(1,11):
    n=int(input())
    secret=list(map(int,input().split()))
    i=1
    while 1:
        if i==6:
            i=1
        tmp=secret[0]
        secret.remove(tmp)

        tmp-=i
        if tmp<=0:
            tmp=0
        secret.append(tmp)

        if tmp==0:


            break
        i+=1
    print("#{} {} {} {} {} {} {} {} {}".format(n, *secret))