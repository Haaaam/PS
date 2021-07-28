n=int(input())
tmp=''
res=''
for i in range(n):
    s=input()
    tmp+=s[0]
    if tmp.count(s[0])>=5:
        if s[0] not in res:
            res+=s[0]
if res:
    print(''.join(sorted(res)))
else:
    print('PREDAJA')