people={(i+1):0 for i in range(5)}

for i in range(5):
    score=list(map(int,input().split()))
    people[i+1]=sum(score)
max_key=max(people,key=people.get)
print(max_key,max(people.values()))