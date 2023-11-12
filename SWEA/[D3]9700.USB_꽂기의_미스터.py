tc=int(input())
# 가장 처음 USB를 꽂을 때, p의 확률로 올바른 면으로 usb를 꽂은 것이고, (1-p)의 확률로는 뒤집어서 usb를 꽂은 것이다.
# q의 확률로 올바른 면을 쥐고 있으면 q의 확률로 정상적으로 usb가 꽂히고 (1-q)의 확률로는 꽂히지 않는다.
# s_1보다 s_2가 더 크면 YES 아니면 NO
# s1=처음 뒷면(1-p)*뒤집어서 꽂고 성공(q) # 한번 뒤집기
# s2=처음에 앞면(p)*실패(1-q)*(앞면 성공 q) # 두번 뒤집기
for t in range(tc):
    p,q=map(float,input().split())
    res='YES'
    s=[(1-p)*q]

    s.append((1-q)*p*q)
    if s[0]<s[1]:
        res='YES'
    else:
        res='NO'
    print(f"#{t+1} {res}")