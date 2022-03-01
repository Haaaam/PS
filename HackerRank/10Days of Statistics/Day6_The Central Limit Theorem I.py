#Central Limit Theorem
import math

x,boxes,mu,sd=int(input()),int(input()),int(input()),int(input())
mu_sum=boxes*mu

sd_sum=math.sqrt(boxes)*sd

def cdf(x,mu,sd):
    Z=(x-mu)/sd
    return 0.5*(1+math.erf(Z/(math.sqrt(2))))

print(round(cdf(x,mu_sum,sd_sum),4))


