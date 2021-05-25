V=int(input())
size=int(input())
arr=list(map(int,input().split()))
def introTutorial(V, arr):
    # Write your code here
    return arr.index(V)
print(introTutorial(V,arr))