t=int(input())
for tc in range(t):
    s=list(input())
    n=['0']*len(s)
    res=0
    for i in range(len(s)):
        if n[i]!=s[i]:
            n[i:]=s[i]*len(n[i:])
            res+=1
    print(f"#{tc+1} {res}")