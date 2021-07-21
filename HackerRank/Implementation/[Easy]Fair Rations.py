def sol(b):
    cnt=0
    for i in range(len(b)):
        try:
            if b[i]%2==1:
                cnt+=2
                b[i+1]+=1
        except:
            return 'NO'
    return cnt
n=int(input())
b=list(map(int,input().split()))
print(sol(b))