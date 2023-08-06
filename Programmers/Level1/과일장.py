def solution(k,m,score):
    ans=0
    score=sorted(score,reverse=True)

    for i in range(0,len(score),m):

        if i+m <=len(score):
            ans+=(min(score[i:i+m])*m)
        else: break
    return ans

k,m=map(int,input().split())
score=[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k,m,score))