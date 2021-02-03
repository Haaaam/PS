a=input()
temp=''
res=''
check=False
for i in a:
    if i==' ':
        res+=temp[::-1]+i
        temp=''
    elif i=='<':
        check=True
        res+=temp[::-1]+i
        temp=''
    elif i=='>':
        check=False
        res+=i
    elif check:
        res+=i
    else:
        temp+=i
res+=temp
print(res)

