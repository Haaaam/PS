'''n=int(input())
arr=[int(input()) for _ in range(n)]
cnt=0
fun=[arr[i]-1 for i in range(1,n)]
f=fun[:]
while fun:
    cnt+=1
    for i in fun:
        if i%fun[0]==0:
            f.remove(i)
    fun=f[:]
print(cnt)
'''

ship=[]

for i in range(int(input())):
    d=int(input())-1
    if d!=0 and all(d%j for j in ship):
        ship.append(d)

print(len(ship))



