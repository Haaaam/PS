#  데이터 ["코드 번호(code)", "제조일(date)", "최대수량(maximum)", "현재 수량("remain)"]
# 조건을 만족하는 데이터만 뽑아서 정렬해야 한다.
# data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬

# 정렬 기준에 해당하는 값이 서로 같은 경우는 없다.
def solution(data, ext, val_ext, sort_by):
    answer = []
    ind = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    for d in range(len(data)):
        if data[d][ind[ext]] >= val_ext:
            pass

        else:

            answer.append(data[d])
    answer = sorted(answer, key=lambda answer: answer[ind[sort_by]])

    return answer

