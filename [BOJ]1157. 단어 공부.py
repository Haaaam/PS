n=input()
res=[0]*26
n=n.upper()
for i in n:
    res[ord(i)-65]+=1
max=res[0]
ans=0
for i in range(1,len(res)):
    if max<res[i]:
        max=res[i]
        ans=i
    elif max==res[i]:
        ans='?'

if ans=='?':
    print(ans)
else:
    print(chr(ans+65))