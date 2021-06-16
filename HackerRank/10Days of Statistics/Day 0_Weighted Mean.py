def weightedMean(X,W):
    tmp=[X[i]*W[i] for i in range(len(X))]
    return sum(tmp)/sum(W)
n=int(input())
X=list(map(int,input().split()))
W=list(map(int,input().split()))
print(round(weightedMean(X,W),1))