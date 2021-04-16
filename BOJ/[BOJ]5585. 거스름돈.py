n=int(input())
res=1000-n
coin=[500,100,50,10,5,1]
cnt=0
for i in coin:
    if res==0:
        break
    cnt+=res//i
    res%=i
print(cnt)