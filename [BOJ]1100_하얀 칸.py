ch =[]
for _ in range(8):
    ch.append(list(input()))

cnt=0
n=-1
for i in ch:
    for j in i:
        n+=1
        if n%2==0:
            if j=='F':
                cnt+=1
    n+=1
print(cnt)
