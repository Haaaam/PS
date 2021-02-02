l=list(input())
stick=0
stack=[]
for i in range(len(l)):
    if l[i]=="(":
        stack.append(l[i])
    else:
        stack.pop()
        if l[i-1]=="(":
            stick+=len(stack)
        else:
            stick+=1

print(stick)

