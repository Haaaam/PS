# a와 b를 모두 재배열한 경우
# a:내림차순 , b: 오름차순
'''n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=0
a.sort(reverse=True)
b.sort()
for i in range(n):
    res+=a[i]*b[i]
print(res)'''

# a만 재배열
# b의 max값을 a와 하나씩 곱하고 곱한다음에는 b에서 가장 큰 값을 제거
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=0
a.sort()
for i in range(n):
    res+=a[i]*max(b)
    b.remove(max(b))
print(res)



