from itertools import combinations
def solution(d,budget):
    cnt=0
    d=sorted(d)
    ans=0
    #for i in range(len(d)):
    for i in range(len(d)):
        cnt += d[i]
        if cnt <= budget:
            ans = i + 1
    return ans
    #for i in range(len(d), 0, -1):
    #    arr = [j for j in list(combinations(d, i)) if sum(j) <= budget]
    #    if len(arr) != 0:
    #        return i


d=[2,2,3,3]
budget=10
cnt=0
d=sorted(d)
ans=0
for i in range(len(d)):
    cnt+=d[i]
    if cnt<=budget:
        ans=i+1
print(ans)
