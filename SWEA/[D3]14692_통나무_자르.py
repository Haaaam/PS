n=int(input())
# n미터의 통나무를 자르는 게임
# 잘린 통나무가 모두 자연수 미터를 가지도록 잘라야 한다.
# 더 이상 자를 수 없게 되는 사람이 진다. 누가 이기는가?

for i in range(n):
    tc=int(input())
    if tc%2==0:
        name="Alice"
    else:
        name="Bob"
    print(f"#{i+1} {name}")