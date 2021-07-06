def sol(s):
    cnt=0

    for i in range(0,len(s),3):
        if s[i]!='S':cnt+=1
        if s[i+1]!='O':cnt+=1
        if s[i+2]!='S':cnt+=1
    return cnt


s=input()
print(sol(s))