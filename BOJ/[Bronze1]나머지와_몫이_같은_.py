#n으로 나누었을 때 나머지와 몫이 같은 모든 자연수의 합

n=int(input())
answer=0
for i in range(1,n):
    answer+=((n)*i+i)
print(answer)