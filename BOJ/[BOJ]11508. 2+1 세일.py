#2021.03.09
#[BOJ]11508. 2+1 세일

n=int(input())
C=sorted([int(input()) for _ in range(n)],reverse=True)
res=0
for i in range(n):
    if i%3!=2:
        res+=C[i]
print(res)

