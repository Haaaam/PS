n,m=map(int,input().split())
array=list(map(int,input().split()))
array.sort()
stack=[]

def sol(index):
    if len(stack)==m:
        print(*stack)
        return

    for i in range(index,n):
        stack.append(array[i])
        sol(i)
        stack.pop()
sol(0)

