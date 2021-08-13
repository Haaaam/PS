#10부제

n=input()
car=list(input().split())
cnt=0
for i in car:
    if n in i:
        cnt+=1
print(cnt)
