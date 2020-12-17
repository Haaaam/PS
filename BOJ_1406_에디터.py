import sys
s=list(sys.stdin.readline().rstrip())
stack=[]

for i in range(int(input())):
    a=sys.stdin.readline().rstrip()
    # L: 커서를 왼쪽으로 한 칸 옮김(커서가 문장의 맨 앞이면 무시)
    if a=="L" and s:
        stack.append(s.pop())
    #D: 커서를 오른쪽으로 한 칸 옮김(커서가 문장의 맨 뒤이면 무시)
    elif a=="D" and stack:
        s.append(stack.pop())
    elif a=="B" and s:
        s.pop()
    elif a[0]=="P":
        s.append(a[2])

print(''.join(s+stack[::-1]))
