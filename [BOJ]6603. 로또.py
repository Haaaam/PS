import sys
from itertools import combinations
input=sys.stdin.readline

check=True
while check:
    array=list(map(int,input().split()))
    n=int(array[0])
    if n==0:
        check=False
        break
    for i in combinations(array[1:],6):
        print(' '.join(map(str,i)))
    print('')