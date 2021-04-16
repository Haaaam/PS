n,m=map(int,input().split())
a,b=input().split()
num=[3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
length=min(n,m)
name=''
for i in range(length):
    name+=a[i]+b[i]
name+=a[length:]+b[length:]

lst=[num[ord(i)-ord('A')]for i in name]
for i in range(n+m-2):
    for j in range(n+m-i-1):
        lst[j]+=lst[j+1]

print(f"{lst[0]%10*10+lst[1]%10}%")

