n=int(input())
a=[]
for i in range(n):
    a.append(input())
l=list(a[0])
for i in range(n):
    for j in range(len(l)):
        if l[j]==a[i][j]:
            continue
        else:
            l[j]='?'
print(''.join(l))
