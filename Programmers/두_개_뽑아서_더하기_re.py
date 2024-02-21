# 정수 배열 numbers가 주어진다.
# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return

def solution(numbers):
    answer=[]
    for i in numbers:
        for j in numbers:
            # 똑같은 수가 두개 이상일 때
            if i==j and numbers.count(i)>1:
                answer.append(i+j)
            elif i!=j and i+j not in answer:
                answer.append(i+j)

    return sorted(set(answer))

numbers=[2,1,3,4,1]
print(solution(numbers))