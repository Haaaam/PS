q=int(input())
for _ in range(q):
    cnt=0
    s=input()
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            cnt+=1
    print(cnt)

