for i in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        print("#%d >"%(i+1))
    elif a==b:
        print("#%d ="%(i+1))
    elif a<b:
        print("#%d <"%(i+1))