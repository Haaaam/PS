for i in range(int(input())):
    n=int(input())
    answer=[[1]]
    for j in range(1,n):
        res=[]
        for k in range(j+1):
            if k==0 or k==j:
                res.append(1)
            else:
                res.append(answer[j-1][k-1]+answer[j-1][k])
        answer.append(res)
    print("#%d" % (i + 1))
    for c in answer:
        print(' '.join(map(str,c)))




