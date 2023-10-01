import math
def solution(slice,n):

    if n % slice != 0:
        answer = (n // slice) + 1
    else:
        answer = (n // slice)
    return answer
# 다른 사람 풀이
# return ((n-1)//slice)+1

slice,n=7,10
# n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇판의 피자를 시켜야 하는가
answer=0
if n%slice!=0:
    answer=(n//slice)+1
else:
    answer=(n//slice)
print(answer)
