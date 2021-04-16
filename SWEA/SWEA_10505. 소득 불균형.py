for i in range(int(input())):
    n=int(input())
    salary=list(map(int,input().split()))
    m=sum(salary)/len(salary)
    cnt=0
    for j in salary:
        if j<=m:
            cnt+=1
    print(f'#{i+1} {cnt}')
