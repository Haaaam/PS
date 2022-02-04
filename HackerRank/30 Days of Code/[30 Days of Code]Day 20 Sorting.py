n=int(input().strip())
a=list(map(int,input().rstrip().split()))
totalSwap=0
for i in range(n):
    numberOfSwaps=0
    for j in range(n-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            numberOfSwaps+=1
    totalSwap+=numberOfSwaps
    if numberOfSwaps==0:
        break
print(f"Array is sorted in {totalSwap} swaps.")
print(f"First Element: {min(a)}")
print(f"Last Element: {max(a)}")