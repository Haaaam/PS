def solution(rank, attendance):

    position = dict()
    for i in range(len(rank)):
        if not attendance[i]:
            pass
        else:
            position[str(i)] = rank[i]
    position = sorted(position.items(), key=lambda x: (x[1], x[0]))
    return 10000*int(position[0][0])+int(position[1][0])*100+int(position[2][0])

rank=[3,7,2,5,4,6,1]
attendance=[False,True,True,True,True,False,False]
position=dict()
for i in range(len(rank)):
    if not attendance[i]:
        pass
    else:
        position[str(i)]=rank[i]
position=sorted(position.items(), key=lambda x:(x[1],x[0]))
print(10000*int(position[0][0])+int(position[1][0])*100+int(position[2][0]))