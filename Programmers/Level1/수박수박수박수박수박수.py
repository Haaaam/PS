def solution(n):
    ans=''
    su,bak='수','박'
    for i in range(n):
        if i%2==0: ans+=su
        else: ans+=bak
    return ans
n=3
su='수'
bak='박'
ans=''
for i in range(n):
    if i%2==0: ans+=su
    else: ans+=bak
print(ans)
