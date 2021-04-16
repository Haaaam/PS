#2021.02.14
#[BOJ]2110. 공유기 설치

n,c=map(int,input().split())
X=sorted([int(input()) for _ in range(n)])
start=1
end=X[-1]-X[0]
res=0
while (start<=end):
    mid=(start+end)//2
    cnt=1
    value=X[0]
    for i in range(1,len(X)):
        if X[i]>=value+mid:
            value=X[i]
            cnt+=1
    if cnt>=c:
        start=mid+1
        res=mid
    else:
        end=mid-1

print(res)


