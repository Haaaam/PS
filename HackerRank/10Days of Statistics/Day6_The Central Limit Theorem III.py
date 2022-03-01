
mean,sig=500,80
muS,sigS=mean,sig/(100**0.5)
L=muS-1.96*sigS
U=muS+1.96*sigS
print(round(L,2))
print(round(U,2))