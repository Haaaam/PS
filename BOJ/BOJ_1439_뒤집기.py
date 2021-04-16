s=list(input())
cnt=0
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        continue
    else:
        cnt+=1
print((cnt)//2)
