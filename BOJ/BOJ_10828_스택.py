import sys
input=sys.stdin.readline
stack=[]
for i in range(int(input())):
    a=input().split()
    if a[0]=="push":
        stack.append(int(a[1]))
    elif a[0]=="top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif a[0]=="size":
        print(len(stack))
    elif a[0]=="empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif a[0]=="pop":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)


