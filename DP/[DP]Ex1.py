#개미전사
'''
조건: 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.
구해야할것: 개미 전사가 얻을 수 있는 식량의 최댓값
점화식
d[i]=max(d[i-1],d[i-2]+array[i])
'''
n=int(input())

array=list(map(int,input().split()))
d=[0]*100

d[0]=array[0]
d[1]=max(array[0],array[1])
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+array[i])
print(d[n-1])