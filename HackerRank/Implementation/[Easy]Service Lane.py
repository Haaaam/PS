def sol(i,t,cases,width):
    for j in range(cases[i][0],cases[i][1]+1):
        tmp.append(width[j])
    return min(tmp)

n,t=map(int,input().split())
width=list(map(int,input().split()))
cases=[list(map(int,input().split())) for i in range(t)]
for i in range(t):
    tmp = []
    print(sol(i,t,cases,width))
