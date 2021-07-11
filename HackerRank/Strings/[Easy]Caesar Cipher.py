n=int(input())
s=input()
k=int(input())
ans=''
for i in s:


    if i.isalpha():
        if i.islower():
            tmp=ord(i)
            if tmp>=122:
                tmp=96
            tmp+=k
            ans+=chr(tmp)
        else:
            
    else:
        ans+=i
print(ans)