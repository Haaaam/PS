
def solution(k, tangerine):
    check = dict()


    answer = 0
    for i in tangerine:
        if str(i) in check:
            check[str(i)] += 1
        else:
            check[str(i)] = 1

    check = sorted(check.items(), key=lambda x: x[1], reverse=True)

    for i in check:
        k -= i[1]
        answer += 1
        if k <= 0:
            break
    return answer
"""
# 다른 사람 풀이
from collections import Counter
def solution(k,tangerine):
    answer=0
    cnt=Counter(tangerine)

    for v in sorted(cnt.values(),reverse=True):
        k-=v
        answer+=1
        if k<=0:
            break
    return answer
    
"""
k = 2
tangerine=[1, 1, 1, 1, 2, 2, 2, 3]
print(solution(k,tangerine))