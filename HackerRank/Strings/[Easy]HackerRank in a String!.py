def sol(s):
    tmp=['h','a','c','k','e','r','r','a','n','k']
    i=0
    while tmp:

        if tmp[0]==s[i]:
           tmp.pop(0)

        i+=1
        if i==len(s):
            break

    if tmp:
        return "NO"
    else:
        return "YES"
n=int(input())
for i in range(n):
    s=input()
    print(sol(s))
