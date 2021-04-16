import sys
input=sys.stdin.readline
res=[]
for i in range(int(input())):
    res.append(list(map(int,input().split())))
res.sort(key=lambda x:(x[1],x[0]))
for i in res:
    print(i[0], i[1])

    
