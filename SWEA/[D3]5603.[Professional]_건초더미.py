tc=int(input())
for t in range(tc):
    n=int(input())
    s=[]
    res=0
    for _ in range(n):
        s.append(int(input()))
    s_avg=sum(s)//len(s)
    for i in range(n):
        if s[i]<s_avg:
            res+=abs(s[i]-s_avg)
    print(f"#{t+1} {res}")
