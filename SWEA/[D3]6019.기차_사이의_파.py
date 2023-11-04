# 두 기차 A,B가 서로를 향해 달리고 있다. 두 기차의 전면부는 250마일 떨어져 있고 기차 A는 시속 10마일, B는 시속 15마일로 달려

# 파리가 기차 A의 전면부에서 기차 B로 시속 20마일의 속력으로 날아간다.
# 파리가 기차 B의 전면부에 닿으면 바로 방향을 바꿔 기차 A를 향해 같은 속력으로 날아간다.
# 그러다 기차 A와 B가 충돌하면 파리는 죽을 것이다. 파리는 죽기 전까지 몇 마일의 거리를 이동했을까?

tc=int(input())
for i in range(tc):
    # a는 기차 a의 속력, b는 기차 b의 속력, f는 파리의 속력이다.
    d,a,b,f=map(int,input().split())

    # 테스트 케이스마다 파리가 이동한 거리를 출력
    # 거리=시간*속력
    print(f"#{i+1} {d/(a+b)*f}")