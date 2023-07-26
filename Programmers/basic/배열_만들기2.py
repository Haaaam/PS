def solution(l,r):
    answer=[]
    for i in range(l,r+1):
        if i%5!=0: continue
        if all(n in ['5', '0'] for n in str(i)):
            answer.append(i)
    if len(answer)==0:
        answer.append(-1)
    return answer

l,r=5,555
answer=[]
for i in range(l,r+1):
    if i%5!=0: continue
    if all(n in ['5', '0'] for n in str(i)):
        answer.append(i)



if len(answer)==0:
    answer.append(-1)

print(answer)