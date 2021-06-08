def luckBalance(k,contests):
    important,unimportant=[],0
    for i,j in contests:
        if j==1:
            important.append(i)
        else:
            unimportant+=i
    if k<len(important):
        tmp=sorted(important)
        x=len(tmp)-k
        return unimportant+sum(tmp[x:])-sum(tmp[:x])
    return unimportant+sum(important)


n,k=map(int,input().split())
contests=[list(map(int,input().split())) for _ in range(n)]

print(luckBalance(k,contests))




