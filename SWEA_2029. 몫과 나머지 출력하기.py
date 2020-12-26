for i in range(int(input())):
    a,b=map(int,input().split())
    print("#%d %d %d"%(i+1,a//b,a%b))