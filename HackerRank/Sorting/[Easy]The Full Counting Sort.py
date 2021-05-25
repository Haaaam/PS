n=int(input())
arr=[]
for i in range(n):
    a=input().split()
    arr.append([int(a[0]),a[1]])
arr=sorted(arr)
print(arr)