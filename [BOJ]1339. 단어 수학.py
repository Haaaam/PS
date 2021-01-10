dic={}
al=[]
for i in range(int(input())):
    al.append(input())

for i in al:
    k=len(i)-1
    for j in i:
        if j in dic:
            dic[j]+=pow(10,k)
        else:
            dic[j]=pow(10,k)

        k-=1
n=[]
for v in dic.values():
    n.append(v)
n.sort(reverse=True)

res,t=0,9
for i in range(len(n)):
    res+=n[i]*t
    t-=1

print(res)

