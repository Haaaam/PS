import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


if __name__ == '__main__':
    n = int(input().strip())
    m, p, z = 0, 0, 0
    arr = list(map(int, input().rstrip().split()))
    for i in arr:
        if i < 0:
            m += 1
        elif i == 0:
            z += 1
        else:
            p += 1
    print(p / n)
    print(m / n)
    print(z / n)
