for i in range(int(input())):
    a=list(input())
    a.sort()
    stack=[]
    for j in a:
        if stack and stack[-1]==j:
            stack.pop()
        else:
            stack.append(j)
    if stack:
        print(f'#{i+1} {"".join(stack)}')
    else:
        print(f'#{i+1} {"Good"}')


