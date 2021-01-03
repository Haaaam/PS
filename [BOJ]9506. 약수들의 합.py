while True:
    n=int(input())
    if n==-1:
        break
    sum=0
    res=[]
    for i in range(1,n):
        if n%i==0:
            sum+=i
            res.append(i)
    res=str(res)
    a=res.replace(","," +").replace("["," = ").replace("]","")
    if sum==n:
        print(str(sum)+a)
    elif n==0:
        print("0 is NOT perfect.")
    else:
        print("%d is NOT perfect."%n)



