s=input()
target=input()
stack=[]

for i in range(len(s)):
    stack.append(s[i])
    if s[i]==target[-1] and ''.join(stack[-len(target):])==target:
        del stack[-len(target):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')
