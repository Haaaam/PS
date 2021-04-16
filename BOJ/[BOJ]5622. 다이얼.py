n=list(input())
res=0
dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for i in n:
    for j in dial:
        if i in j:
            res+=dial.index(j)+2+1

print(res)

