while 1:
    a=input()
    stack=[]
    check=1
    if a=='.':
        break
    for i in a:
        if i=="(":
            stack.append(0)
        elif i=="[":
            stack.append(1)
        elif i==")":
            if len(stack)==0:
                check=0
                break
            if stack.pop()!=0:
                check=0
                break
        elif i=="]":
            if len(stack)==0:
                check=0
                break
            elif stack.pop()!=1:
                check=0
                break
    if len(stack)==0 and check:
            print("yes")
    else:
        print("no")
