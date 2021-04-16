n=int(input())
a=list(map(int,input().split()))
s=sorted(a)
p=[]

for i in a:
    p.append(s.index(i))
    s[s.index(i)]=-1
print(*p)




