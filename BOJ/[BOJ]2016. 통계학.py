import sys
from collections import Counter
input=sys.stdin.readline
n=[]

def mean(num):
    return round(sum(num)/len(num))
def mid(num):
    num.sort()
    return num[len(num)//2]

def sol(num):
    c=Counter(num)
    cnt=c.most_common()
    if len(num)>1:
        if cnt[0][1]==cnt[1][1]:
            s=cnt[1][0]
        else:
            s=cnt[0][0]
    else:
        s=cnt[0][0]

    return s
def ran(num):
    return max(num)-min(num)
for i in range(int(input())):
    n.append(int(input()))
print(mean(n))
print(mid(n))
print(sol(n))
print(ran(n))





