
N=int(input())
X=sorted(list(map(int,input().split())))
s=sum(X)
print(s/len(X))
print(sum(X[len(X)//2-1:len(X)//2+1])/2)
X_cnt=[]
for i in range(len(X)):
    X_cnt.append(X.count(X[i]))
print(X[X_cnt.index(max(X_cnt))])