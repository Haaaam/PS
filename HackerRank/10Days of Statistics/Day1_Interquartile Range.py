from statistics import median
n=int(input())
values=list(map(int,input().split()))
freqs=list(map(int,input().split()))
s=[]
for i in range(len(freqs)):
    for j in range(freqs[i]):
        s.append(values[i])
s=sorted(s)
mid=len(s)//2
if len(s)%2==0:
    low=s[:mid]
    up=s[mid:]
else:
    low=s[:mid]
    up=s[mid+1:]
q1=median(low)
q3=median(up)

print(float(q3-q1))