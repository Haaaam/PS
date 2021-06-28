'''
Problem: What is the probability that the 1st defect
is found during the first 5 inspections?
(처음 5번의 검사에서 첫 번째 결함이 발견될 확률은 얼마나 됩니까?)
'''
def sol(n,p):
    return (1-p)**(n-1)*p

a,b=list(map(int,input().split()))
n=int(input())
res=sum([sol(i,a/b) for i in range(1,n+1)])
print(round(res,3))

