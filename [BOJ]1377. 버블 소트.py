def bubblesort(a,res):
    s=sorted(a)
    for i in range(len(s)):
        res.append(s[i][1]-a[i][1])
    return max(res)+1
n=int(input())
a=[]
res=[]
for i in range(n):
    a.append((int(input()),i))
print(bubblesort(a,res))



