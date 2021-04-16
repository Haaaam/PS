for i in range(int(input())):
    l=list(input())

    for j in range(len(l)):
        if l[j]=='b':
            l[j]='d'
        elif l[j]=='d':
            l[j]='b'
        elif l[j]=='p':
            l[j]='q'
        elif l[j]=='q':
            l[j]='p'
    l.reverse()
    print(f'#{i+1} {"".join(l)}')
