def solution(n,s):
    start,rest=divmod(s,n) # 몫, 나머지
    # ex 2,9일 경우 [4,5] or [5,4]일때가 가장 곱했을때 크기가 크다.
    # 그래서 s를 n으로 나눠줬을 때의 몫만큼 n개의 원소를 가지는 answer list를 생성
    # 나머지 만큼 for문을 돌려 해당하는 answer 원소에 1을 더해준다.
    answer=[start]*n

    if n>s:
       return [-1]
    for i in range(rest):
        answer[i]+=1
    return sorted(answer)

    # 자연수의 개수가 n개일 경우

    """
        for i in range(s, s // 2, -1):
            a, b = i - 1, s + 1 - i
    
            # 각 원소의 합이 s가 되는 수의 집합, 각 원소의 곱이 최대가 되는 집합 찾기
            if (a + b) == s:
                if tmp < a * b:
                    answer = []
                    answer.append(a)
                    answer.append(b)
        
        if len(answer) == 0:
            answer.append(-1)
    return answer
    """

# 집합의 원소의 개수 n과 모든 원소들의 합 s가 매개변수로 주어질 때, 최고의 집합을 return
# 최고의 집합: 각 원소의 합이 S가 되는 수의 집합. 각 원소의 곱이 최대가 되는 집합
# 최고의 집합은 오름차순으로 정렬된 1차원 배열(list, vector)로 return
# 최고의 집합이 존재하지 않는 경우 -1을 return
n,s=2,1
# 집합 중 합이 9가 되는 집합
tmp=0
start,rest=divmod(s,n)


answer=[start]*n

print(rest)
for i in range(rest):
    answer[i]+=1

if len(answer)==0:
    answer.append(-1)

print(sorted(answer))