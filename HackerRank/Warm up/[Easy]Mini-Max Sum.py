#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


arr = sorted(list(map(int, input().split())))
print(sum(arr[:-1]), sum(arr[1:]))