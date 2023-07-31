
def solution(left, right):
    ans=[0]*(right+1)
    res=0
    for i in range(left,right+1):
        for j in range(1,right+1):
            if i%j==0:
                ans[i]+=1
        if ans[i]%2==0:
            res+=i
        else:
            res-=i
    return res

n=13
left,right=13,17
print(solution(left,right))

