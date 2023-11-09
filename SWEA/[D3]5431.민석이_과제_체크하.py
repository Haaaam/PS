tc=int(input())
for t in range(tc):
    n,k=map(int,input().split())
    # 같은 번호가 두 번 이상 주어지는 경우는 없다
    people=list(map(int,input().split()))
    # 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하기
    no=[]
    for i in range(1,n+1):
        if i not in people:
            no.append(i)
    print(f"#{t+1}",*no)