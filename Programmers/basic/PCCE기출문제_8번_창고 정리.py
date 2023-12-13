# 선빈이의 창고에 들어있는 물건의 이름과 개수는 리스트 형태로 주어지며,
# 한 칸에 겹쳐질 수 있는 물건의 개수에는 제한이 없다고 가정

def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i])
            clean_num.append(num[i])

    # 아래 코드에는 틀린 부분이 없습니다.

    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer