#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    cnt=0
    ar=sorted(ar)
    stack=[ar.pop(0)]
    while ar:
        if stack[-1]==ar[0]:
            cnt+=1
            stack.pop()
            del ar[0]
            if ar:
                stack.append(ar[0])
                del ar[0]
            else:
                pass
        elif stack[-1]!=ar[0]:
            stack.append(ar[0])
            del ar[0]
    return cnt

n=int(input())
ar=list(map(int,input().split()))

print(sockMerchant(n,ar))