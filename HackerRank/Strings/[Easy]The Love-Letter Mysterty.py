def sol(s):
    res=0
    for i in range(len(s)//2):
        if s[-(1 + i)] != s[i]:
            res += abs(ord(s[-(1 + i)]) - ord(s[i]))
        else:
            res += 0
    return res

q=int(input())
for _ in range(q):
    s=input()
    res=0
    print(sol(s))
