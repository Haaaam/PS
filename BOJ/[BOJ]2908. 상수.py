a,b=input().split()
res=""
res1=""
for i in range(len(a)-1,-1,-1):
    res+=a[i]
for i in range(len(b)-1,-1,-1):
    res1+=b[i]
if int(res)>int(res1):
    print(int(res))
else:
    print(int(res1))