n=int(input())
grades=[int(input()) for _ in range(n)]
def gradingStudents(grades):
    res=[]
    for i in grades:
        tmp=0
        if i%5==0:
            res.append(i)

        elif i%5!=0:
            tmp+=i+(5-i%5)

            if tmp-i<3 and tmp>=40:
                res.append(tmp)
            else:
                res.append(i)
    return res

for i in gradingStudents(grades):
    print(i)


