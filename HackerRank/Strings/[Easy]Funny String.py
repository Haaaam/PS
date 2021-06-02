'''q=int(input())
for i in range(q):
    s=input()
    tmp=[ord(j) for j in s ]
    ans=[]
    cnt=0
    for k in range(1,len(tmp)):
        ans.append(abs(tmp[k]-tmp[k-1]))
    if list(reversed(ans))==ans:
        print("Funny")
    else:
        print("Not Funny")'''
def funnyString(s):
    tmp=[ord(j) for j in s]
    ans=[]
    for k in range(1,len(tmp)):
        ans.append(abs(tmp[k]-tmp[k-1]))
    if list(reversed(ans))==ans:
        return "Funny"
    else:
        return "Not Funny"
q=int(input())
for i in range(q):
    s=input()
    print(funnyString(s))

