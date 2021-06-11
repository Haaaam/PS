import math
import os
import random
import re
import sys

def findDigits(n):
    s=[int(i) for i in str(n)]
    cnt=0
    for i in s:
        if i==0:
            pass
        elif n%i==0:
            cnt+=1
    return cnt


t=int(input())
for i in range(t):
    n=int(input())
    print(findDigits(n))

