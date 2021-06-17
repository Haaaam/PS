Physics=[15,12,8,8,7,7,7,6,5,3]
History=[10,25,17,11,13,17,20,13,9,15]

P_sum=sum(Physics)/len(Physics)
H_sum=sum(History)/len(History)

P_score=[i-P_sum for i in Physics]
H_score=[i-H_sum for i in History]

n1=sum([x*y for x,y in zip(P_score,H_score)])

P=sum([(x-P_sum)**2 for x in Physics])
H=sum([(y-H_sum)**2 for y in History])

n2=(P**(1/2))*(H**(1/2))

print(round(n1/n2,3))



