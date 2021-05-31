def catAndMouse(x,y,z):
    a=abs(z-x)
    b=abs(z-y)
    if a>b:
        return 'Cat B'
    elif a<b:
        return 'Cat A'
    else:
        return 'Mouse C'

q=int(input())
for i in range(q):

   x,y,z=map(int,input().split())
   print(catAndMouse(x,y,z))

