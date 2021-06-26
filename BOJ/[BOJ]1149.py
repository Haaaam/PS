'''
조건
1. 1번집의 색은 2번 집의 색과 같지 않아야 한다.
2. N번집의 색은 N-1번 집의 색과 같지 않아야 한다.
3. i번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
'''
n=int(input())
house=[]
for i in range(n):
    house.append(list(map(int,input().split())))

for i in range(1,n):
    house[i][0]+=min(house[i-1][1],house[i-1][2])
    house[i][1]+=min(house[i-1][0],house[i-1][2])
    house[i][2]+=min(house[i-1][0],house[i-1][1])
print(min(house[n-1][0],house[n-1][1],house[n-1][2]))