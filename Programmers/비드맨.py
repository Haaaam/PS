n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
s=0
for i in range(len(arr)-1):
    s+=arr[i]
if s==arr[n-1]:
    print(0)
elif s<arr[n-1]:
    print(arr[n-1]-s)
elif (s+arr[n-1])%2==0:
    print(0)
else:
    print(1)




