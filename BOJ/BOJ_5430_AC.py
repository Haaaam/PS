for _ in range(int(input())):
    p=list(input())
    n=int(input())
    if n==0:
        t=input()
        t=[]
    else:
        t=list(map(int,input()[1:-1].split(',')))
    r=False #not reverse
    check=True
    front=0#앞에서부터 버려야 할 것
    rear=0#뒤에서부터 버려야 할 것

    for j in p:
        try:
            if j=="R":
                r=not r
            elif j=="D" and not r:
                 front+=1
            elif j=="D" and r:
                 rear+=1
        except:
            check=False
            print('error')
            break
    if check:

        if front+rear<=n:
            # 안뒤집은 경우
            if not r:
                t=t[front:n-rear]
                print(str(t).replace(' ',''))
            #뒤집은 경우
            else:
                t=t[::-1][rear:n-front]
                print(str(t).replace(' ',''))
        else:
             print('error')






