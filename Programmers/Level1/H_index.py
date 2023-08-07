# 정렬
def solution(citations):
    citations=sorted(citations,reverse=True)
    for i in range(len(citations)):

        if citations[i]<=i:
            return i
    return len(citations)

citations=[3,0,6,1,5]
#citations=sorted(citations) # 0,1,3,5,6
print(solution(citations))