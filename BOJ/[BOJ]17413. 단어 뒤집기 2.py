s=input()
tmp=''
res=''
check=False
for i in s:
    if i==' 'and check==False:
        res+=tmp[::-1]+i
        tmp=''
    elif i=='<':
        check=True
        res+=tmp[::-1]+i
        tmp=''
    elif i=='>':
        check=False
        res+=tmp+i
        tmp=''
    else:
        tmp+=i
res+=tmp[::-1]
print(res)


