# 햄버거 만들기
# 조리된 순서대로 상수의 앞에 아래서부터 위로 쌓이게 된다.
# 상수는 순서에 맞게 쌓여서 완성된 햄버거를 따로 옮겨 포장을 하게 된다.
# 상수가 일하는 가게는 정해진 순서(아래서부터, 빵-야채-고기-빵)로 쌓인 햄버거만 포장을 한다.
# 빵: 1, 야채: 2, 고기: 3
from collections import deque
def solution(ingredient):
    answer = 0
    hamburger=[]
    for i in range(len(ingredient)):
        hamburger.append(ingredient[i])
        if hamburger[-4:]==[1,2,3,1]:
            answer+=1
            del(hamburger[-4:])


    return answer

ingredient=[2,1,1,2,3,1,2,3,1]
print(solution(ingredient))