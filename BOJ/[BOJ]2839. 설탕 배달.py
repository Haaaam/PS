n=int(input())
cnt=0
while 1:
    if n%5==0:
        cnt+=n//5
        break
    n-=3
    cnt+=1
    if n<0:
        cnt=-1
        break
print(cnt)

