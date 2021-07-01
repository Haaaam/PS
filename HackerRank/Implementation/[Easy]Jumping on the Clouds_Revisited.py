n,k=map(int,input().split())
c=list(map(int,input().split()))
e=100
for i in range(0,n,k):
    e-=(2*c[(i+k)%n])+1

print(e)
