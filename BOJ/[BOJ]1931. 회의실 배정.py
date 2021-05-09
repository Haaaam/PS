import sys
input=sys.stdin.readline
n=int(input())
conference=sorted([list(map(int,input().split()))
                   for _ in range(n)], key=lambda x:(x[1],x[0]))
e=cnt=0
for time in conference:
    if time[0]>=e:
        e=time[1]
        cnt+=1
print(cnt)
