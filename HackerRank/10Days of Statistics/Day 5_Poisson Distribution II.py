def solA(a):
    return 160+40*(a+a**2)
def solB(b):
    return 128+40*(b+b**2)

a,b=map(float,input().split())
print(round(solA(a),3))
print(round(solB(b),3))
