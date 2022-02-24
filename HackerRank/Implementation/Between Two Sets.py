import math
import os
import random
import re
import sys

from math import gcd


def getTotalX(a,b):
    max_a=max(a)
    min_b=min(b)
    cnt=0
    for i in range(max_a,min_b+1):
        left=all([i%num_a==0 for num_a in a])
        right=all([num_b%i==0 for num_b in b])
        cnt+=left*right
    return cnt





first_multiple_input=input().rstrip().split()

n=int(first_multiple_input[0])

m=int(first_multiple_input[1])

arr=list(map(int,input().rstrip().split()))

brr=list(map(int,input().rstrip().split()))

total = getTotalX(arr, brr)
print(total)
