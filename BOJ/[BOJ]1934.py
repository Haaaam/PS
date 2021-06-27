def UC1(x,y):
    while y:
        x,y=y,x%y
    return x
def UC2(x,y):
    return (x*y)//(UC1(x,y))
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(UC2(x,y))
