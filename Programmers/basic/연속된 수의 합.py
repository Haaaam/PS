# 연속된 수의 합

def solution(num, total):
    c = total // num
    if num % 2 == 0:
        res = [i for i in range(c - (num // 2) + 1, c + (num // 2) + 1)]
    else:
        res = [i for i in range(c - (num // 2), c + (num // 2) + 1)]
    return res

num = int(input())
total = int(input())


c=total//num
if num%2==0:
    res=[i for i in range(c-(num//2)+1,c+(num//2)+1)]
else:
    res = [i for i in range(c - (num // 2) , c + (num // 2) + 1)]
print(res)



