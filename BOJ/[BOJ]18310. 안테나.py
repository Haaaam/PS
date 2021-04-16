#2021.02.14
#[BOJ]18310. 안테나
n=int(input())
house=sorted(list(map(int,input().split())))
print(house[(n-1)//2])


