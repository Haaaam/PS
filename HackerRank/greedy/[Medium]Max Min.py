import sys
input=sys.stdin.readline
def maxMin(k,arr):
    tmp=sorted(arr)
    return min(tmp[k-1+i]-tmp[i] for i in range(len(arr)-k+1))


n=int(input())
k=int(input())
arr=[int(input()) for _ in range(n)]
print(maxMin(k,arr))
