# 1~n번 상자까지 번호가 증가하는 순서대로 컨테이너 벨트에 일렬로 놓여 영재에게  전달된다.
# 컨테이너 벨트의 맨 앞에 놓인 상자가 현재 트럭에 실어야 하는 순서가 아니라면 그 상자를 트럭에 실을 순서가 될 때까지
# 잠시 다른 곳에 보관해야한다.
# 보조 컨테이너 벨트 추가 설치
# 보조 컨테이너 벨트를 이용해도 기사님이 원하는 순서대로 상자를 싣지 못 한다면, 더이상 상자를 싣지 않는다.
#
"""
def solution(order):
    answer=0
    tmp=[] # 보조컨테이너
    order_l=len(order)
    i=0
    num=0

    while i<order_l:
        # 택배 기사님이 알려준 상자 순서가 현재 택배상자 보다 더 큰 경우
        # 현재 택배상자는 보조 컨테이너 벨트에 보관
        if order[i]>num:
            num+=1
            tmp.append(num)
        # 순서가 같을 경우
        elif order[i]==tmp[-1]:
            tmp.pop()
            i+=1
            answer+=1
        # 보조 컨테이너 벨트에 있는 상자 번호보다 택배에 넣어야할 상자의 번호가 더 작은 경우
        # 이 경우에는 이미 실어야할 택배 상자가 보조 컨테이너 벨트에 담겨 있으므로
        # 현재 실은 상자의 갯수 return
        else:
            return answer


    return answer
"""

# 다른 사람의 풀이
def solution(order):
    answer=0
    stack=[]

    for i,n in enumerate(order):
        stack.append(i+1)

        while stack and stack[-1]==order[answer]:
            stack.pop()
            answer+=1
    return answer
order=[4,3,1,2,5]
print(solution(order))