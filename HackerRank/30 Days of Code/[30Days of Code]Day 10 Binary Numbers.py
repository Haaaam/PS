n=int(input())
data=bin(n)
maximum,current=0,0

for i in data.split('0b')[1]:
    if i=='1':
        current+=1
    else:
        maximum=max(maximum,current)
        current=0
print(max(maximum,current))


