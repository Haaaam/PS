# 매주 월요일과 수요일 오전 9시부터 10시 30분까지 진행되는 당신의 수업에는 N명의 수강생이 잇다.
# 학생들을 몇 개의 조로 나누려고 한다.
# 3명 이상의 학생으로 구성된 조의 수의 최댓값 출력
n=int(input())
for i in range(n):
    n=int(input())

    res=n//3


    print(f"#{i+1} {res}")
