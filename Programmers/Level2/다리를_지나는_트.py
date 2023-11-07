# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 한다.
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 한다.
# 트럭이 최대 bridge_length대 올라갈 수 있다.
# 다리는 weight 이하까지의 무게를 견딜 수 있다.
# 다리에 완전히 오르지 않은 트럭의 무게는 무시한다.
# return: 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지
def solution(bridge_length,weight,truck_weights):
    answer = 0  # 다리를 건너는데 걸리는 시간
    bridge = [0] * bridge_length  # 다리위에 있는 트럭
    tmp = 0
    # 트럭이 지나가는 순서는 정해져 있다.
    truck_weights.reverse()
    while truck_weights:
        answer += 1
        tmp -= bridge.pop(0)
        if tmp + truck_weights[-1] <= weight:
            tmp_truck = truck_weights.pop()
        else:
            tmp_truck = 0
        tmp += tmp_truck
        bridge.append(tmp_truck)
    return answer+len(bridge)

bridge_length=100
weight=100
truck_weights=[10] # 대기중인 트럭
answer=0 # 다리를 건너는데 걸리는 시간
bridge=[0]*bridge_length # 다리위에 있는 트럭
tmp=0
# 트럭이 지나가는 순서는 정해져 있다.
truck_weights.reverse()
while truck_weights:
    answer+=1
    tmp-=bridge.pop(0)
    if tmp+truck_weights[-1]<=weight:
        tmp_truck=truck_weights.pop()
    else:
        tmp_truck=0
    tmp+=tmp_truck
    bridge.append(tmp_truck)


print(answer+len(bridge))






