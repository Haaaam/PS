tc=int(input())
for t in range(tc):
    n=int(input()) # 돌 던지는 사람
    people=list(map(int,input().split()))# 돌이 떨어진 위치
    # 돌이 가장 0에 가깝게 떨어진 곳과 0 사이의 거리 차이와 그렇게 던진 사람이 몇 명인지
    # 나타내는 정수를 공백 하나로 구분하여 출력
    distance,res=[],0
    for p in people:
        distance.append(abs(p-0))
    m=min(distance)
    for d in distance:
        if m==d:
            res+=1

    print("#{} {} {}".format(t+1,m,res))