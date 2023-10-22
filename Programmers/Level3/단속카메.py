
def solution(routes):
    answer=1
    m = 30001
    # 진입지점을 기준으로 정렬
    routes = sorted(routes, key=lambda x: x[0])
    for i in range(len(routes)):
        a, b = routes[i][0], routes[i][1]

        if a > m:
            answer += 1
            m = b
        m=min(m,b)
    return answer

# routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점
# roues[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적여있다.

# [고속도로 진입,고속도로 나간 지점]
# return 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지

# 고속도로를 이동하는 차량의 경로 routes
routes=[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
routes=sorted(routes,key=lambda x:x[0])
answer=0
#print(solution(routes))
m=30000
for i in range(len(routes)):
    a, b = routes[i][0], routes[i][1]

    # 진입지점이 그 전 차량의 진출지점보다 큰 경우
    if a > m:
        answer += 1
        m = b
    m = min(m, b)

print(answer)