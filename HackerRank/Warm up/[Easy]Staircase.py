def staircase(n):
    ans=[]
    for i in range(n):
        ans.append(' '*(n-1-i)+'#'*(i+1))
    return ans
n=int(input())
for i in staircase(n):
    print(i)
