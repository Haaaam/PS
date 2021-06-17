'''python에서 중간값(median)구하기
중간값: 여러 값을 오름차순이나 내림차순으로 늘어놓았을 떄, 맨 가운데에 있는 값.
- 값들의 개수가 짝수이면 가운데 두 값의 산술평균을 중간값으로 선정
- 홀수 있경우는 맨 가운데 값을 중간값으로 선정
'''
from statistics import median
n=int(input())
arr=sorted(list(map(int,input().split())))
mid=len(arr)//2
if len(arr)%2==0:
    low=arr[:mid]
    up=arr[mid:]
else:
    low=arr[:mid]
    up=arr[mid+1:]
print(int(median(low)))
print(int(median(arr)))
print(int(median(up)))

