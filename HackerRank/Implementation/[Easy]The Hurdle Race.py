def hurdleRace(k,height):
    if max(height)<=k:
        return 0
    else:
        return max(height)-k
n,k=map(int,input().split())
height=list(map(int,input().split()))
print(hurdleRace(k,height))