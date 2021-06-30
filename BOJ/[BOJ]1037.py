n=int(input())#n의 진짜 약수의 개수
divisor=list(map(int,input().split()))
divisor.sort()
print(divisor[0]*divisor[-1])