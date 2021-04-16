#2021.03.01
#[BOJ]1748. 수 이어 쓰기 1

n=input()
l=len(n)
res=0

if l==1:
    res=int(n)
else:
    for i in range(l-1):
        res+=9*(10**i)*(i+1)
    res+=(int(n)-(10**(l-1)-1))*l
print(res)

