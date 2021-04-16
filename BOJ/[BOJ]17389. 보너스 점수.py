n=int(input())
x=list(input())
score=0
bonus=0
for i in range(len(x)):
    if x[i]=='X':
        bonus=0
        score+=0
    elif x[i]=='O':
        score+=(i+1)+bonus
        bonus += 1
print(score)


