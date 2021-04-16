import math

m,n=int(input()),int(input())
num1=math.floor(math.sqrt(m))
num2=math.floor(math.sqrt(n))
ans=[i**2 for i in range(num1,num2+1) if i**2>=m and i**2<=n]
if ans:
    print(sum(ans))
    print(min(ans))
else: print(-1)