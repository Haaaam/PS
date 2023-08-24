def solution(n):
    a=bin(n)
    b=n+1
    while str(a).count('1')!=str(b).count('1'):
        if str(a).count('1')==str(bin(b)).count('1'):
            break
        b+=1
    return b

n=15
answer=0
a=bin(n)
print(a)
b=n+1
while str(a).count('1')!=str(b).count('1'):

    if str(a).count('1')==str(bin(b)).count('1'):

        break

    b+=1
print(b)