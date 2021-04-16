#2021.03.03
#[BOJ]1475. 방 번호
n=list(input())
cnt=[0]*10
for i in n:
    cnt[int(i)]+=1
re=cnt[6]+cnt[9]
if re%2==1: re+=1
cnt[6], cnt[9]=re//2,re//2
print(max(cnt))