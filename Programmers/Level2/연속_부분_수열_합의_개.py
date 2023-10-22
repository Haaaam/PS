import itertools
def solution(elements):
    answer = set()
    n = len(elements)

    elements = elements * 2  # 원형 수열이므로 두배로 늘리기기

    for i in range(1, n):
        for j in range(n):
            res = sum(elements[j:j + i])
            answer.add(res)
    return len(answer)+1

# 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가 모두 몇 가지인지 알아보고 싶어졌다.
# 원형 수열: 일반적인 수열에서 처음과 끝이 연결된 형태의 수열
elements=[7,9,1,1,4]
answer=set()
n=len(elements)

elements=elements*2 # 원형 수열이므로 두배로 늘리기기

for i in range(1,n):
    for j in range(n):
        res=sum(elements[j:j+i])
        answer.add(res)

print(len(answer)+1)

