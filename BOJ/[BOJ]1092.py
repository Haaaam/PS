#배
n=int(input()) #크레인의 수
crane=sorted(list(map(int,input().split())),reverse=True)
m=int(input()) #박스의 수
box=sorted(list(map(int,input().split())),reverse=True)

if box[0]>crane[0]:
    print(-1)
    exit()

minutes=0

while box:
    for i in range(n):
        for j in box:
            if crane[i]>=j:
                box.remove(j)
                break
    minutes+=1
print(minutes)

