def funnyString(s):
    tmp=[]
    for i in s:
        tmp.append(ord(i))
    reversed(tmp)
    ans=[]
    for i in range(1,len(tmp)):
        ans.append(abs(tmp[i]-tmp[i-1]))
    cnt=0
    ans.sort()
    for i in range(1,len(ans)):
        if ans[i]==ans[i-1]:
            cnt+=1
    if cnt!=0:
        return "Funny"
    else:
        return "Not Funny"
q=int(input())
for i in range(q):
    s=input()
    print(funnyString(s))