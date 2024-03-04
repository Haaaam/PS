# 어느 과학자의 h-index를 나타내는 값인 h를 구하려고 한다.
# h-index를 구하는 방법
# 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이
# h번 이하 인용되었다면 h의 최댓값이 이 과학자의 h-index이다.
# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때,
# 이 과학자의 h-index를 return 하도록 solution함수 작성하기

def solution(citations):
    answer = 0
    # h-index를 계산하기 위해 내림차순으로 정렬
    citations=sorted(citations,reverse=True)

    for i in range(len(citations)):
        # h-index를 넘는 논문의 갯수
        if citations[i]<=i:
            return i
    # 인용 횟수가 모두 같을 때는 전체를 return
    return len(citations)

citations=[3,0,6,1,5]
print(solution(citations))