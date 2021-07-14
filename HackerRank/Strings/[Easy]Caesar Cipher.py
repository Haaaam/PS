n=int(input())
s=input()
k=int(input())
ans=''
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        if ord(i)+k%26>122:

            ans+=chr(96+(ord(i)+k%26-122))

        else:
            ans+=chr(ord(i)+k%26)

    elif ord(i)>=65 and ord(i)<=90:
        if ord(i)+k%26>90:
            ans+=chr(64+ord(i)+k%26-90)
        else:
            ans+=chr(ord(i)+k%26)
    else:
        ans+=i
print(ans)