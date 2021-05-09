n=int(input())
m=sorted(list(map(int,input().split())))
loss=[]
#짝수일때
if n%2==0:
    for i in range(n//2):
        s=m[i]+m[n-1-i]
        loss.append(s)
#홀수일때
else:
    for i in range(n//2):
        s=m[i]+m[n-2-i]
        loss.append(s)
    loss.append(m[-1])
print(max(loss))

