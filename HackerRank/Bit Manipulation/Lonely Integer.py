import sys
import math
import random
import os
import re

def lonelyinteger(a):
    res=0
    for i in a:
        res ^=i #중복제거연산 ^=

    return res




if __name__=='__main__':
    fptr=open(os.environ['OUTPUT_PATH'],'w')
    n=int(input().strip())
    a=list(map(int,input().rstrip().split()))
    result=lonelyinteger(a)
    print(result)
    fptr.write(str(result)+'\n')
    fptr.close()