n=int(input())
for i in range(n):
    n,a,b=map(int,input().split())

    # p채널과 t채널이 구독자 수 1위를 놓고 치열한 경쟁을 벌이고 있다.
    # n명의 사람에게 질문
    # return p채널과 t채널 모두 구독하고 있는 사람들이 최소 몇 명, 최대 몇 명인지 구하는 프로그램을 작성하라
    min_p=0
    max_p=min(a,b) # 최대 구독자 수

    # 최소 구독자 수
    if a+b>n:
        min_p=(a+b)-n

    print(f"#{i+1} {max_p} {min_p}")