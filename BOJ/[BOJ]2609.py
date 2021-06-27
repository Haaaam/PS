'''
유크리리드 호제법: 두 수 사이의 최대공약수를 구하는 알고리즘
'''
#최대공약수와 최소공배수
def UC1(x,y):
    while y:
        x,y=y,x%y
    return x
def UC2(x,y):
    return (x*y)//UC1(x,y)
a,b=map(int,input().split())
print(UC1(a,b))
print(UC2(a,b))

