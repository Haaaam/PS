'''
표준편차(sd): 평균으로부터 보통거리를 나타내는 값
신뢰구간: 모수가 어느 범위 안에 있는지를 확률적으로 보여주는 방법(표본에서 산출된 통계와 함께 제공된다)
- ex) 신뢰수준 95%에서 투표자의 35%~45%가 A후보를 지지하고 있다.
- 이용되는 표본의 크기가 크면 클수록 신뢰구간은 점점 더 좁아진다.

'''

import math
n=int(input())
x=sorted(list(map(int,input().split())))
m=sum(x)/n #Mean(n)
print(m)
median=sum(x[n//2-1:n//2+1])/2
print(median)#Median of this array
# Mode
x_cnt=[x.count(x[i]) for i in range(n)]
mode=x[x_cnt.index(max(x_cnt))]
print(mode)

# Standard Deviation(SD)
sd_sum=0
for i in x:
    sd_sum+=(i-m)**2
sd=round(math.sqrt(sd_sum/n),1)
print(sd)
lower_confidence=m-1.96*sd/len(x)**0.5
upper_confidence=m+1.96*sd/len(x)**0.5
# Confidence Interval for the mean
print(round(lower_confidence,1),round(upper_confidence,1))


