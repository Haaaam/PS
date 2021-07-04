for _ in range(int(input())):
    s1,s2=input(),input()
    check="YES"
    for i in s1:
        if i in s2:
            check="YES"
            break
        else:
            check="NO"
    print(check)
