# 2016년 1월 1일은 금요일

week=['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
days=[31,29,31,30,31,30,31,31,30,31,30,31]
n=int(input())
for i in range(n):
    m,d=map(int,input().split())

    # 해당 달의 일 수를 sum(days[:m-1])로 계산 1월인 경우 계산 X
    res=(sum(days[:m-1])+d)%7
    ans=(res+4-1)%7
    print(f"#{i+1} {ans}")

