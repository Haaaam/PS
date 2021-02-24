#2021.02.24
#[BOJ]1946. 신입 사원

import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n = int(input())
    person=sorted([list(map(int,input().split())) for _ in range(n)])
    cnt=0
    min=person[0][1]
    for j in range(1,len(person)):
        if person[j][1]<min:
            cnt+=1
            min=person[j][1]
    print(cnt+1)



