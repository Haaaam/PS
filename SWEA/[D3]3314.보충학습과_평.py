# 학생 수 다섯 명
# 점수가 40점 이상인 학생은 점수 그대로, 40점 미만은 보충학습 받아서 40점으로 올릴 수 있다.
n=int(input())
for i in range(n):
    score=list(map(int,input().split()))
    stack=[i for i in score if i>=40]
    low=[i for i in score if i<40]
    print(f"#{i+1} {(sum(stack)+40*len(low))//5}")