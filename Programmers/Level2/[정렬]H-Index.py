citations=list(map(int,input().split()))


def solution(citations):
    citations = sorted(citations, reverse=True)

    for i in range(len(citations)):
        if citations[i] <= i:
            return i

    return len(citations)

print(solution(citations))