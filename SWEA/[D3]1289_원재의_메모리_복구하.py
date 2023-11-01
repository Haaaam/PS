n=int(input())
for j in range(n):
    memory=input() # 원래값
    init=['0']*len(memory)# 초기화 상태

    res=0
    #  메모리 bit중 하나를 골라 0인지 1인지 결정하면 해당 값이 메모리의 끝까지 덮어씌워지도록 해야한다.
    for i in range(len(init)):
        if init[i]!=memory[i]:
            init[i:]=memory[i]*len(init[i:])

            res+=1



    print(f"#{j+1} {res}")