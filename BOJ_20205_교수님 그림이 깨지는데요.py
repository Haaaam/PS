#가로/세로 길이:N, 이미지 늘릴 배수:K
n,k=map(int,input().split())
pixel=""
for i in range(n):
    a=input().split()
    res=""
    for j in a:
        res+=(j+" ")*k
    pixel+=(res+"\n")*k
print(pixel)



