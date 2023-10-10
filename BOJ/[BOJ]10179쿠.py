n=int(input())

for i in range(n):
    cost=float(input())
    answer=cost-(cost*(20/100))
    print("${:.2f}".format(round(answer,2))) # Double 대신 :.2f로 표현