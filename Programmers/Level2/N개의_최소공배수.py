import math
def solution(arr):
    while len(arr) >= 2:
        a = arr.pop()
        b = arr.pop()
        arr.append((a*b)//math.gcd(a,b))
    return arr[0]

arr=[2,6,8,14]

while len(arr) >= 2:
    a = arr.pop()
    b = arr.pop()
    arr.append((a * b) // math.gcd(a, b))
print(arr[0])