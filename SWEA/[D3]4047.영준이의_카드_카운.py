tc=int(input())

for t in range(tc):
    s=input()
    # 이미 겹치는 카드가 있다면 문자열 ERROR을 출력
    check=[13]*4
    tmp=[]
    for i in range(len(s)//3):

        if s[i*3:i*3+3] in tmp:
            check="ERROR"
            break

        else:
            tmp.append(s[i*3:i*3+3])
            if s[i*3]=='S':
                check[0]-=1
            elif s[i*3]=='D':
                check[1]-=1
            elif s[i*3]=='H':
                check[2]-=1
            elif s[i*3]=='C':
                check[3]-=1

    if check=="ERROR":
        print(f"#{t+1}",check)
    else:
        print(f"#{t+1}", *check)