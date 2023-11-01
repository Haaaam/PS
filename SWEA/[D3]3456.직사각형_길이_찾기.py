# 직사각형의 네 변 중에서 세 변의 길이가 주어진다.
# 나머지 한 변의 길이가 얼마인지 출력하는 프로그램을 작성하라
tc=int(input())
for i in range(tc):
    a,b,c,=map(int,input().split())
    res=0
    if a==b==c:
        res=a
    elif a!=b and b==c:
        res=a
    elif a==b and b!=c:
        res=c
    elif a==c and a!=b:
        res=b
    print(f"#{i+1} {res}")