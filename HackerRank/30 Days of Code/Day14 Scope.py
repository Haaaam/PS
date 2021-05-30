class Difference:
    def __init__(self,a):
        self.__elements=a
        self.maximumDifference=0

    def computeDifference(self):
        self.maximumDifference=max(self.__elements)-min(self.__elements)

n=int(input())
a=list(map(int,input().split()))

d=Difference(a)
d.computeDifference()
print(d.maximumDifference)