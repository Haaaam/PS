s=input()
target=input()
last=target[-1]
stack=[]

for i in range(len(s)):
    stack.append(s[i])
    if s[i]==last and ''.join(stack[-len(target):])==target:
        del stack[-len(target):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')
