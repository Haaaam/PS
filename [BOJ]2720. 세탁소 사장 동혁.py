#2021.03.09
#[BOJ]2720. 세탁소 사장 동혁

coin=[25,10,5,1]
for _ in range(int(input())):
    money=int(input())
    list={25:0,10:0,5:0,1:0}
    while money:
        for i in coin:
            while money>=i:
                money-=i
                list[i]+=1
    print(*list.values())
