n=int(input())
for i in range(n):
    s=input()
    # 두개의 서로 다른 문자가 등장하고, 각 문자가 정확히 두분 등장하는지 판단
    tmp=set(s)
    check=[]
    res=''
    if len(tmp)<2:
        res="No"
    else:
        for j in tmp:
            t=s.count(j)
            if t==2:
                res='Yes'
            else:
                res='No'
                break


    print(f"#{i+1} {res}")