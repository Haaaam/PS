def solution(n, control):

    for i in control:
        if i=="w":
            n+=1
        elif i=="s":
            n-=1
        elif i=="a":
            n-=10
        elif i=="d":
            n+=10

    return n
n=0
control="wsdawsdassw"
print(solution(n,control))
