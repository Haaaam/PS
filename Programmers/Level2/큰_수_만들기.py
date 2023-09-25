def solution(number, k):
    number = [int(i) for i in number]
    answer=[]
    for i in number:

        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1

        answer.append(i)

    return ''.join(str(i) for i in answer[:len(number)-k])

number="999"
# k개의 수를 제거했을 때 얻을 수 있는 가장 큰 수
number=[int(i) for i in number]
k=2
print(solution(number,k))






