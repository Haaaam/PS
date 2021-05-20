n=int(input())
scores=list(map(int,input().split()))
'''score_max,score_min=scores[0],scores[0]
max_cnt,min_cnt=0,0
for i in range(1,n):
    if scores[i]>score_max:
        score_max=scores[i]
        max_cnt+=1
    if scores[i]<score_min:
        score_min=scores[i]
        min_cnt+=1
print(max_cnt,min_cnt)'''
def breakingRecords(scores,n):
    # Write your code here
    score_max,score_min=scores[0],scores[0]
    cnt=[0,0]
    for i in range(1,n):
        if scores[i]>score_max:
            score_max=scores[i]
            cnt[0]+=1
        if scores[i]<score_min:
            score_min=scores[i]
            cnt[1]+=1
    return cnt
print(*breakingRecords(scores,n))
