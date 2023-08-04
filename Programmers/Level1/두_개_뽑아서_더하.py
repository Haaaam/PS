from collections import Counter

def solution(numbers):
    ans = []
    for i in numbers:
        for j in numbers:
            if i==j:
                if numbers.count(i)>1 and numbers.count(j)>1:
                    ans.append(i+j)
            else:
                ans.append(i+j)
    return sorted(list(set(ans)))




