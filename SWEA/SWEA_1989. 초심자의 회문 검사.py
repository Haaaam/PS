for i in range(int(input())):
    a=input()
    if a[0]==a[-1]:
        print("#%d %d"%(i+1,1))
    else:
        print("#%d %d"%(i+1,0))
