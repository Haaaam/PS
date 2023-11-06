# 1이상 n이하의 정수가 적혀 있는 길
# p가 최솟값도, 최댓값도 아니라면 p_i를 평범한 숫자라고 정의한다.
# 주어진 순열에서 평범한 숫자의 개수는 몇개 인가?
tc=int(input())
for i in range(tc):
    n=int(input())
    p=list(map(int,input().split()))
    res=0
    for j in range(1,len(p)-1):
        if (p[j]>p[j-1] and p[j]<p[j+1]) or (p[j]<p[j-1] and p[j]>p[j+1]):
            res+=1

    print(f"#{i+1} {res}")