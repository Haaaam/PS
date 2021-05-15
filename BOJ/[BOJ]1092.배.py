n=int(input())
crane=sorted(list(map(int,input().split())),reverse=True)
m=int(input())
box=sorted(list(map(int,input().split())),reverse=True)
pos=[0]*n
if max(crane)<max(box):
    print(-1)
else:
    for i in range(n):
        while pos[i]<len(box):
            if crane[i]>box[i] and
    print(cnt)
