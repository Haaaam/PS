for i in range(10):
    test=int(input())
    number=[list(map(int,input().split())) for _ in range(100)]
    res=[]
    for j in range(len(number)):
        res.append(sum(number[j]))

    for x in range(len(number)):
        sum_col=0
        for y in range(len(number)):
            sum_col+=number[y][x]
        res.append(sum_col)

    sum_left=0
    sum_right=0
    for x in range(len(number)):
        for y in range(len(number)):
            if x==y:
                sum_left+=number[x][y]
            if y==len(number)-x:
                sum_right+=number[x][y]
    res.append(sum_left)
    res.append(sum_right)



    print(f"#{i+1} {max(res)}")


