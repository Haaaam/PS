n=int(input())
def fact():
    if n==0:
        return 0
    cnt=0
    for i in range(2,n+1):
        if i%5==0:
            cnt+=1
        if i%25==0:
            cnt+=1
        if i%125==0:
            cnt+=1
    return cnt
print(fact())

