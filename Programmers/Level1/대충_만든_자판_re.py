# 동일한 키를 연속해서 빠르게 누르면 할당된 순서대로 문자가 바뀐다.
# return 각 문자열을 작성하기 위해 키를 최소 몇 번씩 눌러야 하는지 순서대로 배열에 담기
# 단, 목표 문자열을 작성할 수 없을 때는 -1을 저장
def solution(keymap, targets):
    answer = []
    for t in targets: # target에 있는 단어
        cnt=0
        for c in t: # 문자 한개씩 keymap에 있는지 확인
            check=False # target 문자열을 자판으로 만들 수 있는지 확인
            key_len=101 # 최대 key길이가 100이므로 101로 설정
            for key in keymap:
                if c in key:
                    key_len=min(key.index(c)+1,key_len) # 각 문자열을 작성하기 위해 키를 누르는 횟수를 최소로 만들기
                    check=True
            if not check: # keymap에 target 단어가 없을 경우 -1을 정답에 담기
                cnt=-1
                break
            cnt+=key_len
        answer.append(cnt)

    return answer

keymap=["ABACD","BCEFD"]
targets=["ABCD","AABB"]
print(solution(keymap,targets))