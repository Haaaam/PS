# 용사가 몬스터를 공격할 때는 기본적으로 D만큼의 데미지를 입힌다.
# 용사가 익힌 공격의 레벨 L에 따라 추가적인 데미지가 있는데,
# 몬스터를 때린 횟수가 n번이라고 하면, 다음 공격이 몬스터에게 입히는 데미지는 D(1+n*L%)가 된다.
# return 총 n번의 공격을 하면 몬스터에게 가한 총 데미지가 몇이 되는지 구하는 프로그램
tc=int(input())
for j in range(1,tc+1):
    d,l,n=map(int,input().split())
    res=0


    for i in range(n):
        res+=d*(1+i*(l/100))

    print(f"#{j} {int(res)}")