def minimumDistances(a):
    idx = list()
    res = list()
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                idx.append([i,j])
    for i, (m,n) in enumerate(idx):
        res.append(abs(m-n))
    if not res:
        return -1
    else:
        return min(res)



n=int(input())
a=list(map(int,input().split()))
print(minimumDistances(a))