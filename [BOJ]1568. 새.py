#2021.02.12
#[BOJ]1568. 새

n=int(input())
sec=0
k=1
while n!=0:
    if n<k: k=1
    n-=k
    sec+=1
    k+=1
print(sec)