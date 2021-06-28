import math

def sol(X_mean,k):
    global e
    return (X_mean**k)*e**(-X_mean)/(math.factorial(k))


X_mean,k=float(input()),int(input())
e=2.71828
print(round(sol(X_mean,k),3))