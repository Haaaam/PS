grade=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for i in range(int(input())):
    n,k=map(int,input().split())
    score=[]
    for j in range(n):
        m,f,t=map(int,input().split())
        res=m*0.35+f*0.45+t*0.20
        score.append(res)
    k_score=score[k-1]
    score.sort(reverse=True)
    rank=score.index(k_score)//(n//10)
    k_grade=grade[rank]
    print('#{} {}'.format(i+1,k_grade))

    