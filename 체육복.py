n=int(input())
lost=list(map(int,input().split()))
reserve=list(map(int,input().split()))
#cnt=0
#s=[]
#for i in range(1,n+1):
#    if i not in lost and reserve:
#        s.append(i)
#        cnt+=1
#for i in lost:
#    for j in reserve:
#        if i+1==j or i-1==j:
#            s.append(i)
#            reserve.remove(j)
#            cnt+=1

#print(cnt)
def solution(n,lost,reserve):
    cnt=0
    for i in range(1,n+1):
        if i not in lost:
            cnt+=1
        elif i in reserve:
            cnt+=1
            reserve.remove(i)
            lost.remove(i)
    for i in lost:
            if i-1 in reserve:
                reserve.remove(i-1)
                cnt+=1
            elif i+1 in reserve:
                reserve.remove(i+1)
                cnt+=1

    return cnt
print(solution(n,lost,reserve))

