n=int(input())
j=0
for i in range(n,0,-1):
    print(" "*j+"*"*((2*i)-1))
    j+=1
for i in range(2,n+1):
    print(" "*(n-i)+"*"*((2*i)-1))
