for i in range(int(input())):
    l=input()
    for j in range(1,11):
        if l[0:j]==l[j:j*2]:
            print("#%d %d"%(i+1,j))
            break
        else:
            continue