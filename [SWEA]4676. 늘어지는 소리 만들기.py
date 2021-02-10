#2021.02.10
#[SWEA][D3]4676. 늘어지는 소리 만들기

for i in range(int(input())):
    s=list(input())
    h=int(input())
    n=list(map(int,input().split()))
    n.sort(reverse=True)
    for j in n:
        s.insert(j,'-')
    print(f"#{i+1} {''.join(s)}")