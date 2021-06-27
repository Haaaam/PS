def countingValleys(steps,path):
    sealevel=valley=0
    for i in range(steps):
        if path[i]=='U':
            sealevel+=1
        else:
            sealevel-=1
        if sealevel==0 and path[i]=='U':
            valley+=1
    return valley
steps=int(input())
path=list(input())
print(countingValleys(steps,path))