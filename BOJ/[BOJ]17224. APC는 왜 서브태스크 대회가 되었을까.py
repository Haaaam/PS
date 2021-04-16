n,l,k=map(int,input().split())
problem=[]
score=0
for i in range(n):
    sub1,sub2=map(int,input().split())
    problem.append([sub1,sub2])
problem=sorted(problem, key=lambda x:(x[1],x[0]))

for i in range(len(problem)):
    if k==0:
        break
    elif k!=0 and problem[i][0]<=l:
        if problem[i][1]<=l:
            score+=140
        else:
            score+=100
        k-=1
print(score)

