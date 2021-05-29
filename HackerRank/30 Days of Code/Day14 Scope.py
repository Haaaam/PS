class Difference:
    
n=int(input())
a=list(map(int,input().split()))

d=Difference(a)
d.computeDifference()
print(d.maximumDifference)