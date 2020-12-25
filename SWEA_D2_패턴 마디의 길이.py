for i in range(int(input())):
    t=list(input())
    for j in range(1,11):
        if t[0:j]==t[j:j*2]:
            print("#%d %d"%(i+1,j))
            break
        else:
            continue