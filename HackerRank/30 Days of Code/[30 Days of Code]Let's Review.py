t=int(input())
for _ in range(t):
    S=input()
    o,tt='',''
    for i in range(len(S)):
        if i%2==0:
            o+=S[i]
        else:
            tt+=S[i]
    print(f'{o} {tt}')


