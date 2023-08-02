def solution(s):
    ans=''
    s=s.split(' ')
    for w in s:
        for i in range(len(w)):
            if i % 2 == 0:
                ans += w[i].upper()
            else:
                ans += w[i].lower()
        ans+=' '
    return ans[:-1]
s="try hello world"
print(solution(s))